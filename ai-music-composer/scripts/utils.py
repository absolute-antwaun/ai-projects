from music21 import converter, instrument, note, chord
import os

def extract_notes_from_midi(midi_dir):
    notes = []

    for file in os.listdir(midi_dir):
        if not file.endswith(".mid") and not file.endswith(".midi"):
            continue

        midi = converter.parse(os.path.join(midi_dir, file))

        parts = instrument.partitionByInstrument(midi)
        elements = parts.parts[0].recurse() if parts else midi.flat.notes

        for element in elements:
            if isinstance(element, note.Note):
                notes.append(str(element.pitch))
            elif isinstance(element, chord.Chord):
                notes.append('.'.join(str(n) for n in element.normalOrder))

    return notes