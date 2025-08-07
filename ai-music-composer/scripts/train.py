import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
import numpy as np

from models.lstm_model import MusicLSTM
from scripts.utils import extract_notes_from_midi
from scripts.preprocess import prepare_sequences

# === Load and preprocess ===
notes = extract_notes_from_midi("data/midi")  # <-- put your MIDIs here
sequence_length = 50
X, y, vocab_size = prepare_sequences(notes, sequence_length)

# Convert to tensors
X_tensor = torch.tensor(X, dtype=torch.long)
y_tensor = torch.tensor(y, dtype=torch.long)

dataset = TensorDataset(X_tensor, y_tensor)
loader = DataLoader(dataset, batch_size=64, shuffle=True)

# === Model Setup ===
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MusicLSTM(vocab_size).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# === Training ===
epochs = 30
for epoch in range(epochs):
    total_loss = 0
    for batch_X, batch_y in loader:
        batch_X, batch_y = batch_X.to(device), batch_y.to(device)

        optimizer.zero_grad()
        outputs, _ = model(batch_X)
        loss = criterion(outputs[:, -1, :], batch_y)
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    print(f"Epoch {epoch+1}/{epochs} - Loss: {total_loss:.4f}")

# Save model
torch.save(model.state_dict(), "models/music_lstm.pth")
