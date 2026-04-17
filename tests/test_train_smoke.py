import lightning as L

from ml_cookbook.data.dummy_datamodule import DummyDataModule
from ml_cookbook.models.prototype_model import PrototypeModel


def test_lightning_smoke_train() -> None:
    dm = DummyDataModule(
        batch_size=4,
        input_shape=(3, 16, 16),
        num_classes=5,
        train_samples=16,
        val_samples=8,
        num_workers=0,
    )
    model = PrototypeModel(
        input_shape=(3, 16, 16),
        hidden_dim=16,
        num_classes=5,
        learning_rate=1e-3,
    )

    trainer = L.Trainer(
        max_epochs=1,
        accelerator="cpu",
        devices=1,
        enable_progress_bar=False,
        logger=False,
        limit_train_batches=2,
        limit_val_batches=1,
        enable_checkpointing=False,
    )
    trainer.fit(model=model, datamodule=dm)

    assert trainer.state.finished
