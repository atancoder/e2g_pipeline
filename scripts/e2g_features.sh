#!/bin/bash
set -e

CONFIG_FILE=config/config.yaml
E2G_FEATURES_REPO=$(yq '.E2G_FEATURES_REPO' $CONFIG_FILE | tr -d '"')
ABC_RESULTS_DIR=$(readlink -f $(yq '.ABC_RESULTS' $CONFIG_FILE | tr -d '"' ))
E2G_FEATURES_RESULTS=$(readlink -f $(yq '.E2G_FEATURES_RESULTS' $CONFIG_FILE | tr -d '"' ))
BIOSAMPLES_TABLE_FILE=$(yq '.ABC_biosamples_table' $CONFIG_FILE | tr -d '"')
E2G_FEATURES_CONFIG_NAME="$PWD/config/dataset_config.tsv"

# Generate config from ABC output
python scripts/gen_e2g_features_config.py --abc_biosamples_config $BIOSAMPLES_TABLE_FILE --abc_results_dir $ABC_RESULTS_DIR --output_config_name $E2G_FEATURES_CONFIG_NAME

cd $E2G_FEATURES_REPO
# snakemake --use-conda --profile slurm --config dataset_config=$E2G_FEATURES_CONFIG_NAME --rerun-incomplete
snakemake --use-conda -j2 --config dataset_config=$E2G_FEATURES_CONFIG_NAME results_dir=$E2G_FEATURES_RESULTS --rerun-incomplete