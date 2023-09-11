#!/bin/bash
set -e

echo "Running ABC"
./scripts/abc.sh 

echo "Running ENCODE-rE2G"
./scripts/e2g_features.sh 
