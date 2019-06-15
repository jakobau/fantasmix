melody_rnn_generate \
--config=melody_rnn \
--bundle_file=./scripts/Magenta/Models/attention_rnn.mag \
--output_dir=./scripts/Magenta/SecondOutput \
-—num_outputs=1 \
--num_steps=128 \
--primer_midi=./scripts/Magenta/Output/FirstOutput.mid 
