from __future__ import annotations

import argparse
from pathlib import Path

import lightning as L
import yaml
from lightning.pytorch.callbacks import (
    EarlyStopping,
    LearningRateMonitor,
    ModelCheckpoint,
)
from lightning.pytorch.loggers import CSVLogger

from ml_cookbook.data.dummy_datamodule import DummyDataModule
from ml_cookbook.models.prototype_model import PrototypeModel
from ml_cookbook.utils.repro import seed_everything


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Train a minimal Lightning prototype."
    )
    parser.add_argument(
        "--config",
        type=Path,
        default=Path("configs/default.yaml"),
        help="Path to the YAML config file.",
    )
    return parser.parse_args()


def load_config(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def main() -> None:
    args = parse_args()
    cfg = load_config(args.config)

    seed = int(cfg.get("seed", 42))
    deterministic = bool(cfg.get("trainer", {}).get("deterministic", True))
    seed_everything(seed=seed, deterministic=deterministic)

    data_cfg = cfg["data"]
    model_cfg = cfg["model"]
    trainer_cfg = cfg["trainer"]

    input_shape = tuple(data_cfg["input_shape"])
    num_classes = int(data_cfg["num_classes"])

    datamodule = DummyDataModule(
        batch_size=int(data_cfg["batch_size"]),
        input_shape=input_shape,
        num_classes=num_classes,
        train_samples=int(data_cfg["train_samples"]),
        val_samples=int(data_cfg["val_samples"]),
        test_samples=int(data_cfg["test_samples"]),
        num_workers=int(data_cfg["num_workers"]),
    )

    model = PrototypeModel(
        input_shape=input_shape,
        hidden_dim=int(model_cfg["hidden_dim"]),
        num_classes=num_classes,
        learning_rate=float(model_cfg["learning_rate"]),
    )

    exp_name = cfg.get("experiment_name", "baseline")
    logger = CSVLogger(save_dir="logs", name=exp_name)

    callbacks = [
        ModelCheckpoint(
            monitor="val_loss",
            mode="min",
            save_top_k=1,
            filename="best",
        ),
        EarlyStopping(monitor="val_loss", mode="min", patience=3),
        LearningRateMonitor(logging_interval="epoch"),
    ]

    trainer = L.Trainer(
        max_epochs=int(trainer_cfg["max_epochs"]),
        accelerator=trainer_cfg.get("accelerator", "auto"),
        devices=trainer_cfg.get("devices", 1),
        deterministic=bool(trainer_cfg.get("deterministic", True)),
        log_every_n_steps=int(trainer_cfg.get("log_every_n_steps", 1)),
        enable_progress_bar=bool(trainer_cfg.get("enable_progress_bar", True)),
        limit_train_batches=trainer_cfg.get("limit_train_batches", 1.0),
        limit_val_batches=trainer_cfg.get("limit_val_batches", 1.0),
        callbacks=callbacks,
        logger=logger,
    )

    trainer.fit(model=model, datamodule=datamodule)
    trainer.test(model=model, datamodule=datamodule, ckpt_path="best")


if __name__ == "__main__":
    main()
