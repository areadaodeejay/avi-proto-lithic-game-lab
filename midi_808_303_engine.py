import random
from midiutil import MIDIFile

try:
    from midi2audio import FluidSynth
    HAS_FLUIDSYNTH = True
except ImportError:
    HAS_FLUIDSYNTH = False

# ===============================================
# MIDI 808 + Ring Mod + TB-303 Style Engine
# For Frequency Warriors & Proto-Lithic Game Lab
# Now with WAV export support!
# ===============================================

class Midi808303Engine:
    def __init__(self, bpm=140):
        self.bpm = bpm
        self.track = 0
        self.channel_drum = 9   # Standard MIDI drum channel
        self.channel_bass = 0
        self.channel_lead = 1
        
    def create_808_pattern(self, midi, duration=4):
        """Classic 808 drum pattern (4 bars)"""
        # Kick (36), Snare (38), Closed Hat (42), Open Hat (46)
        kick = [1,0,0,0, 1,0,0,1, 1,0,0,0, 1,0,0,0] * duration
        snare = [0,0,1,0, 0,0,1,0, 0,0,1,0, 0,1,0,0] * duration
        ch_hat = [1,1,1,1, 1,1,1,1, 1,1,1,1, 1,1,1,1] * duration
        oh_hat = [0,0,0,0, 0,0,0,0, 0,0,0,0, 1,0,0,0] * duration
        
        time = 0
        for i in range(len(kick)):
            if kick[i]:
                midi.addNote(self.track, self.channel_drum, 36, time, 0.5, 110)  # Kick
            if snare[i]:
                midi.addNote(self.track, self.channel_drum, 38, time, 0.5, 100)  # Snare
            if ch_hat[i]:
                midi.addNote(self.track, self.channel_drum, 42, time, 0.25, 80)   # Closed hat
            if oh_hat[i]:
                midi.addNote(self.track, self.channel_drum, 46, time, 0.8, 70)    # Open hat
            time += 0.25
        
    def create_303_bassline(self, midi, root_note=36, length=16):
        """TB-303 style acid bassline"""
        notes = []
        current_note = root_note
        for i in range(length):
            if random.random() < 0.7:
                current_note = root_note + random.choice([-3, -1, 0, 2, 4, 7])
            notes.append(current_note)
        
        time = 0
        for note in notes:
            velocity = random.randint(95, 115)
            # Portamento / glide effect (common in 303)
            midi.addNote(self.track, self.channel_bass, note, time, 0.5, velocity)
            time += 0.5
    
    def add_ring_mod_lead(self, midi, length=32):
        """Ring modulation style lead (metallic, inharmonic tones)"""
        time = 0
        for _ in range(length):
            base = random.choice([60, 64, 67, 72])
            # Simulate ring mod by adding dissonant interval
            ring_tone = base + random.choice([6, 7, 11, 13])
            midi.addNote(self.track, self.channel_lead, base, time, 0.25, 90)
            midi.addNote(self.track, self.channel_lead, ring_tone, time, 0.25, 65)
            time += 0.25
    
    def generate_track(self, filename="proto_lithic_808_303.mid", bars=8, export_wav=False):
        """Generate full MIDI track. Optionally export to WAV."""
        midi = MIDIFile(1)
        midi.addTempo(self.track, 0, self.bpm)
        
        # Add 808 drums
        self.create_808_pattern(midi, duration=bars)
        
        # Add 303 bass
        self.create_303_bassline(midi, root_note=36, length=bars*8)
        
        # Add ring-mod lead
        self.add_ring_mod_lead(midi, length=bars*16)
        
        with open(filename, "wb") as output_file:
            midi.writeFile(output_file)
        
        print(f"✅ Generated MIDI: {filename} | BPM: {self.bpm} | Bars: {bars}")
        
        if export_wav:
            self.export_to_wav(filename)
        
        return filename

    def export_to_wav(self, midi_filename, output_wav=None):
        """Export MIDI to WAV using FluidSynth (if available)"""
        if not HAS_FLUIDSYNTH:
            print("⚠️  midi2audio / FluidSynth not installed.")
            print("   Install with: pip install midi2audio")
            print("   Also need FluidSynth installed on your system.")
            return None
        
        if output_wav is None:
            output_wav = midi_filename.replace('.mid', '.wav')
        
        try:
            fs = FluidSynth()
            fs.midi_to_audio(midi_filename, output_wav)
            print(f"✅ Exported WAV: {output_wav}")
            return output_wav
        except Exception as e:
            print(f"❌ Error exporting WAV: {e}")
            return None


# ======================
# Quick Test / Usage
# ======================
if __name__ == "__main__":
    engine = Midi808303Engine(bpm=138)
    midi_file = engine.generate_track("frequency_warriors_808_303.mid", bars=8, export_wav=True)
    print("MIDI 808 + 303 Ring-Mod engine with WAV export ready for game integration!")
    print("Tip: pip install midi2audio for WAV support")
