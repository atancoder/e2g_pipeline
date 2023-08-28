#!/bin/bash

set -e

CONFIG_FILE=config/config.yaml
BIOSAMPLES_TABLE_FILE=$(yq '.ABC_biosamples_table' $CONFIG_FILE | tr -d '"')
ABC_RESULTS_DIR=$(readlink -f $(yq '.ABC_RESULTS' $CONFIG_FILE | tr -d '"' ))
ABC_REPO=$(yq '.ABC_REPO' $CONFIG_FILE | tr -d '"')

cd $ABC_REPO
snakemake --use-conda -j3 --config biosamplesTable=$BIOSAMPLES_TABLE_FILE predictions_results_dir=$ABC_RESULTS_DIR --rerun-incomplete

# snakemake --use-conda --profile slurm --config biosamplesTable=$BIOSAMPLES_TABLE_FILE predictions_results_dir=$ABC_RESULTS_DIR --rerun-incomplete
