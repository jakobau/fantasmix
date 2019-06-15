How to Use:

Input the following parameters in the UserInput text file in the following order
-Tempo
-Scale
-Instrument 
-Length
-Name
type sh run.sh
It should output the file with the given name to the Third Output Folder

How it Works:
It first runs the midiClass file which creates a short melody line
It then clears the previous outputs in the Output Folder and run loopback.sh which takes that primer midi created by midiClass and lengthens it
It puts the names of those newly created files into a text file called files.txt
It then runs firstOutputRenamer.py and clears the previous outputs in the SecondOutput Folder
It then runs lengthChanger and Based on the inputed user length it runs attention.sh and lengthens midi file to the desired length
It once again puts all the created file into the files.txt file and runs secondOutputRenamer.py
Finally it runs midoConverter and using the mido packages reads the created midi file and creates a new one with the desired instrument and name

