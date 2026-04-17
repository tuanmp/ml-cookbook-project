from __future__ import annotations

import lightning as L
import torch
from torch import nn


class PrototypeModel(L.LightningModule):
    """Minimal classifier baseline for cookbook experiments."""

    def __init__(
        self,
        input_shape: tuple[int, ...] = (3, 32, 32),
        hidden_dim: int = 128,
        num_classes: int = 10,
        learning_rate: float = 1e-3,
    ) -> None:
        super().__init__()
        self.save_hyperparameters()

        input_dim = 1
        for d in input_shape:
            input_dim *= d

        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, num_classes),
        )
        self.loss_fn = nn.CrossEntropyLoss()

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.ndim != 4:
            raise ValueError(
                f"Expected input with 4 dims (B, C, H, W), got {x.shape}"
            )
        return self.net(x)

    def _shared_step(
        self,
        batch: tuple[torch.Tensor, torch.Tensor],
        stage: str,
    ) -> torch.Tensor:
        x, y = batch
        logits = self(x)
        loss = self.loss_fn(logits, y)
        acc = (logits.argmax(dim=1) == y).float().mean()

        self.log(
            f"{stage}_loss",
            loss,
            prog_bar=True,
            on_epoch=True,
            on_step=False,
        )
        self.log(
            f"{stage}_acc",
            acc,
            prog_bar=True,
            on_epoch=True,
            on_step=False,
        )
        return loss

    def training_step(
        self,
        batch: tuple[torch.Tensor, torch.Tensor],
        batch_idx: int,
    ) -> torch.Tensor:
        del batch_idx
        return self._shared_step(batch, stage="train")

    def validation_step(
        self,
        batch: tuple[torch.Tensor, torch.Tensor],
        batch_idx: int,
    ) -> torch.Tensor:
        del batch_idx
        return self._shared_step(batch, stage="val")

    def test_step(
        self,
        batch: tuple[torch.Tensor, torch.Tensor],
        batch_idx: int,
    ) -> torch.Tensor:
        del batch_idx
        return self._shared_step(batch, stage="test")

    def configure_optimizers(self) -> torch.optim.Optimizer:
        return torch.optim.Adam(
            self.parameters(),
            lr=self.hparams.learning_rate,
        )
