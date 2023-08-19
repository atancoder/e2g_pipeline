#!/bin/bash
set -e

cd $E2G_FEATURES_REPO
snakemake --use-conda --profile slurm