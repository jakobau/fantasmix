import os
f = open("./scripts/Magenta/files.txt", "r")
x = f.readline()
x = x.strip("\n")
os.rename("./scripts/Magenta/Output/"+x, "./scripts/Magenta/Output/FirstOutput.mid")
