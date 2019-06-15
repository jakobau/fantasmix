import os
import subprocess
from scripts.Magenta.Scripts.MidoConverter import midoP
from scripts.Magenta.Scripts.midiClass import *

class runMagenta():
    def __init__(self, tempo, scale, instrument , length, name):
        self.tempo = tempo
        self.scale = scale
        self.instrument = instrument
        self.length = length
        self.name = name
        self.midi = midi(self.tempo, self.scale, self.instrument, self.length, self.name)
        self.midoP = midoP(self.tempo, self.scale, self.instrument, self.length, self.name)

    def runMain(self):
        nameList = []
        nameList2 = []

        #os.system("python ./scripts/Magenta/Scripts/midiClass.py")
        #midi = midi(self.tempo, self.scale, self.instrument, self.length, self.name)
        self.midi.runProgram()

        os.system("rm -rf ./scripts/Magenta/Output/*")
        os.system("sh ./scripts/Magenta/Scripts/Lookback.sh")

        #cd ./scripts/Magenta/Output
        #Ls > ./scripts/Magenta/files.txt
        nameList = os.listdir("./scripts/Magenta/Output")

        #python ./scripts/Magenta/Scripts/firstOutputRenamer.py
        os.rename("./scripts/Magenta/Output/" + nameList[0], "./scripts/Magenta/Output/FirstOutput.mid")


        os.system("rm -rf ./scripts/Magenta/SecondOutput/*")

        #python ./scripts/Magenta/Scripts/LengthChanger.py
        #sh ./scripts/Magenta/Scripts/attention.sh
        #python ./scripts/Magenta/Scripts/LengthReverter.py
        if self.length == "short":
            os.system("sh ./scripts/Magenta/Scripts/attentionShort.sh")
            os.system("echo it is working ---------------")
        elif self.length == "mid":
            os.system("sh ./scripts/Magenta/Scripts/attentionMid.sh")
            os.system("echo it is working ---------------")
        elif self.length == "long":
            os.system("sh ./scripts/Magenta/Scripts/attentionLong.sh")
            os.system("echo it is working ---------------")

        #cd ./scripts/Magenta/SecondOutput
        #ls > ./scripts/Magenta/files.txt
        nameList2 = os.listdir("./scripts/Magenta/SecondOutput")

        #python ./scripts/Magenta/Scripts/secondOutputRenamer.py
        os.rename("./scripts/Magenta/SecondOutput/"+nameList2[0], "./scripts/Magenta/SecondOutput/SecondOutput.mid")

        self.midoP.runMido()
        #midi = midi(self.tempo, self.scale, self.instrument, self.length, self.name)
        #midi.runProgram()

#test = runMagenta("slow","major","bird","mid","ifThisWorksIAmAGenius3")
#test.runMain()
