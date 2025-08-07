![Build](https://github.com/absolute-antwaun/ai-music-composer/actions/workflows/python-app.yml/badge.svg)
![License](https://img.shields.io/github/license/absolute-antwaun/ai-music-composer)
![Stars](https://img.shields.io/github/stars/absolute-antwaun/ai-music-composer?style=social)
![Last Commit](https://img.shields.io/github/last-commit/absolute-antwaun/ai-music-composer)

# 🎼 AI Music Composer 🎶
*A Dark Sci-Fi Ambient Music Generator Using LSTM & MIDI*

This project is a neural network-based music composer that generates otherworldly, ambient sci-fi soundscapes using Long Short-Term Memory (LSTM) networks trained on MIDI files.

---

## 🚀 Project Highlights

- 🎹 Converts MIDI music into sequences of notes
- 🧠 Trains an LSTM neural network to learn musical structure
- 🎼 Generates brand new ambient sci-fi compositions
- 🧰 Easily extendable with your own MIDI dataset
- 🧪 Future GitHub Actions integration for testing/linting

---

## 🧠 Model Overview

- **Architecture:** 3-layer LSTM with embedding
- **Input:** Sequences of notes (as integers)
- **Output:** Probabilities for next note prediction
- **Framework:** PyTorch

---

## 📂 Project Structure

ai-music-composer/
├── data/
│ └── midi/ # Place your MIDI files here
├── models/
│ └── lstm_model.py # LSTM architecture
├── scripts/
│ ├── preprocess.py # MIDI → Note Sequences
│ ├── train.py # Training pipeline
│ └── utils.py # Helper functions
├── README.md # You're here!
└── requirements.txt

---

## ⚙️ How to Train the Model

# 1. Install requirements
pip install -r requirements.txt

# 2. Add MIDI files to /data/midi

# 3. Train the model
python scripts/train.py

---

🔮 Roadmap

Music generation script
Custom dataset builder
GitHub Actions + linting
Web interface for live generation

📜 License: MIT License – use this for any creative or educational purpose ✨

🧙‍♂️ Inspiration: Inspired by sci-fi soundscapes in Blade Runner, Annihilation, and Arrival. This is a sandbox for dark ambient AI creativity.


