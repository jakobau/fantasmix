python ./scripts/Magenta/Scripts/midiClass.py

rm -rf ./scripts/Magenta/Output/*
sh ./scripts/Magenta/Scripts/Lookback.sh

cd ./scripts/Magenta/Output
ls > ./scripts/Magenta/files.txt

python ./scripts/Magenta/Scripts/firstOutputRenamer.py

rm -rf ./scripts/Magenta/SecondOutput/*

python ./scripts/Magenta/Scripts/LengthChanger.py
sh ./scripts/Magenta/Scripts/attention.sh
python ./scripts/Magenta/Scripts/LengthReverter.py

cd ./scripts/Magenta/SecondOutput
ls > ./scripts/Magenta/files.txt
python ./scripts/Magenta/Scripts/secondOutputRenamer.py

python ./scripts/Magenta/Scripts/MidoConverter.py
