import os
f = open("./scripts/Magenta/files.txt", "r")
x = f.readline()
x = x.strip("\n")
os.rename("./scripts/Magenta/SecondOutput/"+x, "./scripts/Magenta/SecondOutput/SecondOutput.mid")
