
---

### 🧬 `mnist-pytorch-starter/model_card.md`

```markdown
# 🧬 Model Card: MNIST CNN (PyTorch)

## 📌 Intended Use

This model classifies grayscale handwritten digits (0-9) from the MNIST dataset. It's designed for educational use and experimentation.

## 🧠 Model Architecture

- Input: (1, 28, 28)
- Conv2D (32 filters) + ReLU + MaxPool
- Conv2D (64 filters) + ReLU + MaxPool
- Flatten → Linear (128) + ReLU → Dropout → Linear (10)

## 🛠️ Training Details

- Framework: PyTorch
- Optimizer: Adam
- Loss Function: CrossEntropyLoss
- Epochs: 5-20
- Batch Size: 64

## 📊 Performance

| Metric     | Value   |
|------------|---------|
| Accuracy   | ~98%    |
| Loss       | 0.02-0.05 |
| Inference  | <10ms   |

## ⚠️ Limitations

- Only trained on MNIST (not generalizable to other handwriting datasets)
- Not adversarially robust
- Lightweight model not suitable for production

## 👤 Author

Antwaun Westerfield
