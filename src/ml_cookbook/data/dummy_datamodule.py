from __future__ import annotations

import lightning as L
import torch
from torch.utils.data import DataLoader, Dataset


class DummyDataset(Dataset):
    """Random dataset used to validate training plumbing and tensor shapes."""

    def __init__(
        self,
        num_samples: int,
        input_shape: tuple[int, ...],
        num_classes: int,
    ) -> None:
        self.num_samples = num_samples
        self.input_shape = input_shape
        self.num_classes = num_classes

    def __len__(self) -> int:
        return self.num_samples

    def __getitem__(self, idx: int) -> tuple[torch.Tensor, torch.Tensor]:
        x = torch.randn(self.input_shape, dtype=torch.float32)
        y = torch.randint(0, self.num_classes, size=(), dtype=torch.long)
        return x, y


class DummyDataModule(L.LightningDataModule):
    """LightningDataModule with train/val/test random data."""

    def __init__(
        self,
        batch_size: int = 16,
        input_shape: tuple[int, ...] = (3, 32, 32),
        num_classes: int = 10,
        train_samples: int = 256,
        val_samples: int = 64,
        test_samples: int = 64,
        num_workers: int = 0,
    ) -> None:
        super().__init__()
        self.batch_size = batch_size
        self.input_shape = input_shape
        self.num_classes = num_classes
        self.train_samples = train_samples
        self.val_samples = val_samples
        self.test_samples = test_samples
        self.num_workers = num_workers

        self.train_ds: DummyDataset | None = None
        self.val_ds: DummyDataset | None = None
        self.test_ds: DummyDataset | None = None

    def setup(self, stage: str | None = None) -> None:
        if stage in (None, "fit"):
            self.train_ds = DummyDataset(
                self.train_samples,
                self.input_shape,
                self.num_classes,
            )
            self.val_ds = DummyDataset(
                self.val_samples,
                self.input_shape,
                self.num_classes,
            )
        if stage in (None, "test"):
            self.test_ds = DummyDataset(
                self.test_samples,
                self.input_shape,
                self.num_classes,
            )

    def train_dataloader(self) -> DataLoader:
        if self.train_ds is None:
            raise RuntimeError(
                "Call setup('fit') before requesting train_dataloader"
            )
        return DataLoader(
            self.train_ds,
            batch_size=self.batch_size,
            shuffle=True,
            num_workers=self.num_workers,
            pin_memory=torch.cuda.is_available(),
        )

    def val_dataloader(self) -> DataLoader:
        if self.val_ds is None:
            raise RuntimeError(
                "Call setup('fit') before requesting val_dataloader"
            )
        return DataLoader(
            self.val_ds,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers,
            pin_memory=torch.cuda.is_available(),
        )

    def test_dataloader(self) -> DataLoader:
        if self.test_ds is None:
            raise RuntimeError(
                "Call setup('test') before requesting test_dataloader"
            )
        return DataLoader(
            self.test_ds,
            batch_size=self.batch_size,
            shuffle=False,
            num_workers=self.num_workers,
            pin_memory=torch.cuda.is_available(),
        )
