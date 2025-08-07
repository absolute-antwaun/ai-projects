import pickle
import numpy as np
from scripts.utils import extract_notes_from_midi

def prepare_sequences(notes, sequence_length):
    # Map notes to integers
    pitch_names = sorted(set(notes))
    note_to_int = {note: number for number, note in enumerate(pitch_names)}

    network_input = []
    network_output = []

    for i in range(len(notes) - sequence_length):
        seq_in = notes[i:i + sequence_length]
        seq_out = notes[i + sequence_length]
        network_input.append([note_to_int[n] for n in seq_in])
        network_output.append(note_to_int[seq_out])

    n_patterns = len(network_input)

    network_input = np.reshape(network_input, (n_patterns, sequence_length))
    network_output = np.array(network_output)

    # Save mappings
    with open("data/note_to_int.pkl", "wb") as f:
        pickle.dump(note_to_int, f)

    return network_input, network_output, len(pitch_names)
