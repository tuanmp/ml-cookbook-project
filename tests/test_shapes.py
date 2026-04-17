import torch

from ml_cookbook.data.dummy_datamodule import DummyDataModule
from ml_cookbook.models.prototype_model import PrototypeModel


def test_dummy_batch_shapes() -> None:
    dm = DummyDataModule(batch_size=4, input_shape=(3, 32, 32), num_classes=10)
    dm.setup("fit")
    x, y = next(iter(dm.train_dataloader()))

    assert x.shape == (4, 3, 32, 32)
    assert y.shape == (4,)
    assert y.dtype == torch.long


def test_model_forward_shape() -> None:
    model = PrototypeModel(
        input_shape=(3, 32, 32),
        hidden_dim=32,
        num_classes=10,
    )
    x = torch.randn(4, 3, 32, 32)
    logits = model(x)

    assert logits.shape == (4, 10)
