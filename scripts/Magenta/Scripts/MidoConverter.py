import mido
from midiutil import MIDIFile

"""f = open("./scripts/Magenta/UserInput.txt", "r")
userTempo = f.readline().strip("\n")
f.readline()
instrument = f.readline().strip("\n")
f.readline()
name = f.readline().strip("\n")
"""

class midoP():
    def __init__(self, userTempo, scale, instrument, length, name):
        self.name = name

        if instrument == "piano":
            self.program = 1
        elif instrument == "guitar":
            self.program = 25
        elif instrument == "bass":
            self.program = 33
        elif instrument == "violin":
            self.program = 41
        elif instrument == "synth":
            self.program = 89
        elif instrument == "banjo":
            self.program = 106
        elif instrument == "glockenspiel":
            self.program = 10
        elif instrument == "marimba":
            self.program = 13
        elif instrument == "choir":
            self.program = 54
        elif instrument == "trombone":
            self.program = 58
        elif instrument == "saxophone":
            self.program = 67
        elif instrument == "clarinet":
            self.program = 13
        elif instrument == "bird":
            self.program = 123
        elif instrument == "bagpipes":
            self.program = 109
        elif instrument == "helicopter":
            self.program = 122
        elif instrument == "telephone":
            self.program = 124
        elif instrument == "SynthDrums":
            self.program = 118

        if userTempo == "slow":
            self.tempo = 40
        elif userTempo == "mid":
            self.tempo = 60
        elif userTempo == "fast":
            self.tempo = 80
        elif userTempo == "faster":
            self.tempo = 120

    def runMido(self):
        mid = mido.MidiFile('./scripts/Magenta/SecondOutput/SecondOutput.mid')

        onOff = []
        notes = []
        time = []
        trackTime = 0
        program = 0
        tempo = 60

        MyMIDI = MIDIFile(1)
        MyMIDI.addProgramChange(0,0, 0, self.program)
        MyMIDI.addTempo(0, 0, self.tempo)

        print("start")
        for msg in mid.play():
            onOff.append(msg.type)
            time.append(msg.time)
            test = msg.bytes()
            notes.append(test[1])
        print("finished")

        for i in range(0, len(notes)):
            MyMIDI.addNote(0, 0, notes[i], trackTime + time[i], 1, 100)
            trackTime += time[i]

        with open("static/audio/" + self.name + ".mid", "wb") as output_file:
                    MyMIDI.writeFile(output_file)
