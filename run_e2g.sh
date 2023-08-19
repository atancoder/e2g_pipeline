#!/bin/bash
set -e

conda activate e2g_pipeline

./abc.sh 
./e2g_features.sh 
python run_encode_e2g.py