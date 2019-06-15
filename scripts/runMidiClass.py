import random
from midiutil import MIDIFile
import os.path
random.seed()


class midi():
    def __init__(self, tempo, scale, intrument, length, name):
        self.track = 0
        self.channel = 0
        self.time = 0
        self.duration = 1
        self.name = name + ".mid"

        if intrument == "piano":
            self.program = 1
        elif intrument == "guitar":
            self.program = 28
        elif intrument == "bass":
            self.program = 33
        elif intrument == "violin":
            self.program = 41
        elif intrument == "synth":
            self.program = 89
        elif intrument == "banjo":
            self.program = 106

        if tempo == "slow":
            self.tempo = 40
        elif tempo == "mid":
            self.tempo = 60
        elif tempo == "fast":
            self.tempo = 80
        elif tempo == "faster":
            self.tempo = 120

        if scale == "major":
            self.scale = [48, 50, 52, 53, 55, 57, 59, 60, 62, 64, 65, 67, 69, 71, 72, 74, 76, 77, 79, 81, 83]
        elif scale == "minor":
            self.scale = [48, 50, 51, 53, 55, 56, 58, 60, 62, 63, 65, 67, 68, 70, 72, 74, 75, 77, 79, 80, 82]

        self.length = length
        self.volume = 100

    def createFile(self):
        MyMIDI = MIDIFile(1)
        MyMIDI.addProgramChange(self.track, self.channel, self.time, self.program)
        MyMIDI.addTempo(self.track, self.time, self.tempo)
        return MyMIDI

    def createMotif(self):
        length = random.randint(5, 10)
        motifPitch = []
        motifTime = []
        previous = 60
        upPercent = 50
        consecutive = 1
        time = 0
        scale = self.scale
        previousJump = 0
        previousTimeInterval = 0
        for i in range(0, length):
            intervalType = random.randint(0, 100)
            upDown = random.randint(0, 100)
            y = scale.index(previous)
            if upDown > upPercent:
                upDown = -1
                upPercent += 2 * consecutive
                consecutive += 1
            else:
                upDown = 1
                upPercent += -2 * consecutive
                consecutive += 1
            y = scale.index(previous)
            try:
                if intervalType <= 25:
                    pitch = previous
                elif intervalType <= 27:
                    upDown = -1 * previousJump
                    pitch = scale[y + 7*upDown]
                elif intervalType <= 75:
                    pitch = scale[y + 1*upDown]
                else:
                    skipInterval = random.randint(0, 100)
                    if intervalType <= 25:
                        pitch = scale[y + 4*upDown]
                    elif intervalType <= 27:
                        pitch = scale[y + 3*upDown]
                    elif intervalType <= 75:
                        pitch = scale[y + 2*upDown]
                    else:
                        pitch = scale[y + 5*upDown]
            except IndexError:
                upDown *= -1
                if intervalType <= 25:
                    pitch = previous
                elif intervalType <= 27:
                    pitch = scale[y + 7*upDown]
                elif intervalType <= 75:
                    pitch = scale[y + 1*upDown]
                else:
                    skipInterval = random.randint(0, 100)
                    if intervalType <= 25:
                        pitch = scale[y + 4*upDown]
                    elif intervalType <= 27:
                        pitch = scale[y + 3*upDown]
                    elif intervalType <= 75:
                        pitch = scale[y + 2*upDown]
                    else:
                        pitch = scale[y + 5*upDown]
            timeInterval = random.randint(0, 100)
            if timeInterval <= 10:
                if previousTimeInterval == 1:
                    time = time + 1/4
                    previousTimeInterval = 1/4
                else:
                    time = time + 1/16
                    previousTimeInterval = 1/16
            elif timeInterval <= 41:
                if previousTimeInterval == 1:
                    time = time + 1/4
                    previousTimeInterval = 1/4
                else:
                    time = time + 1/8
                    previousTimeInterval = 1/8
            elif timeInterval <= 81:
                time = time + 1/4
                previousTimeInterval = 1/4
            elif timeInterval <= 88:
                time = time + 1/4 + 1/8
                previousTimeInterval = 1/8 + 1/4
            elif timeInterval <= 97:
                if previousTimeInterval == 1/16:
                    time = time + 1/4
                    previousTimeInterval = 1/4
                else:
                    time = time + 1/2
                    previousTimeInterval = 1/2
            elif timeInterval <= 100:
                if previousTimeInterval == 1/16:
                    time = time + 1/2
                    previousTimeInterval = 1/2
                else:
                    time = time + 1
                    previousTimeInterval = 1
            motifPitch.append(pitch)
            motifTime.append(time)
            previous = pitch
            previousJump = upDown
        return motifPitch, motifTime

    def addMotif(self, pitch, time, trackTime, MyMIDI):
        for i in range(0, len(pitch)):
            MyMIDI.addNote(self.track, self.channel, pitch[i], trackTime + time[i], self.duration, self.volume)
        return trackTime + time[len(time)-1]

    def runProgram(self):
        MyMIDI = self.createFile()
        trackTime = 0
        if self.length == "short":
            pitch_A, time_A = self.createMotif()
            pitch_B, time_B = self.createMotif()
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
        elif self.length == "mid":
            pitch_A, time_A = self.createMotif()
            pitch_B, time_B = self.createMotif()
            pitch_C, time_C = self.createMotif()
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_C, time_C, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
        elif self.length == "long":
            pitch_A, time_A = self.createMotif()
            pitch_B, time_B = self.createMotif()
            pitch_C, time_C = self.createMotif()
            pitch_D, time_D = self.createMotif()
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_C, time_C, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_C, time_C, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_A, time_A, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_C, time_C, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_D, time_D, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)
            trackTime = self.addMotif(pitch_B, time_B, trackTime, MyMIDI)

        # {% load static %}
        # save_path = "{% static 'audio/' %}"
        save_path = "static/audio/" + self.name

        with open(save_path, "wb") as output_file:
            MyMIDI.writeFile(output_file)


"""
test = midi("mid", "major", "guitar", "mid", "guitar")
test.runProgram()
test2 = midi("mid", "minor", "piano", "long", "does it work")
test2.runProgram()
"""
