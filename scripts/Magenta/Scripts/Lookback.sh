#!/bin/bash
melody_rnn_generate \
--config=melody_rnn \
--bundle_file=./scripts/Magenta/Models/lookback_rnn.mag  \
--output_dir=./scripts/Magenta/Output \
-—num_outputs=1 \
--num_steps=64 \
--primer_midi=./scripts/Magenta/primer.mid
