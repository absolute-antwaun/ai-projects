# 🧠 Model Card: AI Music Composer

## 🏷️ Model Name
`MusicLSTM-v1`

## 🧾 Model Description
`MusicLSTM-v1` is a Long Short-Term Memory (LSTM) neural network designed to generate ambient, dark sci-fi music by predicting note sequences from MIDI data. It learns temporal musical patterns and generates novel compositions that resemble the training data in structure, but not exact form.

---

## 📊 Model Details

| Field            | Description                                         |
|------------------|-----------------------------------------------------|
| Architecture     | 3-layer LSTM with Embedding + Dropout               |
| Framework        | PyTorch                                             |
| Input            | Sequences of note tokens (as integer IDs)           |
| Output           | Probability distribution over next note             |
| Loss Function    | CrossEntropyLoss                                    |
| Optimizer        | Adam (lr=0.001)                                     |
| Training Data    | Public MIDI files (ambient / sci-fi inspired)       |
| Sequence Length  | 50 notes (default)                                  |
| Epochs           | 50 (can be adjusted)                                |
| Batch Size       | 64 (default)                                        |

---

## 📁 Intended Use

| Use Case                     | Intended? |
|------------------------------|-----------|
| Ambient music generation     | ✅        |
| Sci-fi film scoring drafts   | ✅        |
| Soundscape exploration       | ✅        |
| Commercial music production  | ⚠️ (Not guaranteed unique output) |
| Real-time performance        | ❌        |

---

## 🧪 Evaluation

Evaluation is qualitative:
- Generated samples are subjectively judged based on:
  - 🎼 Musical coherence
  - 🔁 Repetition avoidance
  - 🎧 Atmosphere & vibe
  - 🛸 Alignment with genre (dark sci-fi, ambient)

Future additions:
- BLEU-style sequence similarity scoring
- MIDI→WAV→Spectrogram comparison

---

## 🧱 Limitations

- Training data heavily affects output quality.
- Repetitive or too-short datasets result in bland music.
- Not suitable for real-time inference on edge devices.
- Doesn’t understand musical theory or emotion directly.

---

## 📦 Training Configuration

```json
{
  "embedding_dim": 100,
  "hidden_dim": 256,
  "num_layers": 2,
  "dropout": 0.3,
  "learning_rate": 0.001,
  "epochs": 50,
  "batch_size": 64
}

🔐 Ethical Considerations

    No copyrighted MIDI files were used in training.

    Generated music may resemble training data but is not copied.

    Always verify originality before public or commercial use.


🧰 Authors & Credits

    Model developed by Antwaun Westerfield

    Inspired by research in symbolic music generation using RNNs and LSTMs


📌 Version

Model version: v1.0
Last updated: August 2025
Status: In Development