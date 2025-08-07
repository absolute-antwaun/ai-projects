import torch
from train import Net  # Ensure your CNN class is named `Net`

def test_output_shape():
    model = Net()
    dummy_input = torch.rand(1, 1, 28, 28)
    output = model(dummy_input)
    assert output.shape == (1, 10)
