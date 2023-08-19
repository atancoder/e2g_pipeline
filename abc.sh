#!/bin/bash

set -e

CONFIG_FILE=config.yaml
BIOSAMPLES_TABLE_FILE=$(yq '.ABC_biosamples_table' $CONFIG_FILE)
ABC_REPO=$(yq '.ABC_REPO' $CONFIG_FILE | tr -d '"')

cd $ABC_REPO

snakemake --use-conda --profile slurm --config biosamplesTable=$BIOSAMPLES_TABLE_FILE