import os
f = open("./scripts/Magenta/UserInput.txt", "r")
f.readline()
f.readline()
f.readline()
length = f.readline().strip("\n")
if length == "short":
    os.rename("./scripts/Magenta/Scripts/attention.sh", "./scripts/Magenta/Scripts/attentionShort.sh")
elif length == "mid":
    os.rename("./scripts/Magenta/Scripts/attention.sh", "./scripts/Magenta/Scripts/attentionMid.sh")
elif length == "long":
    os.rename("./scripts/Magenta/Scripts/attention.sh", "./scripts/Magenta/Scripts/attentionLong.sh")
