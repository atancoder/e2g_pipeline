import glob
import os

import click
import pandas as pd

CONFIG_TEMPLATE_FILE = "https://raw.githubusercontent.com/EngreitzLab/encode_e2g_features/main/config/dataset_config_template.tsv"


@click.command()
@click.option("--abc_biosamples_config", type=str, required=True)
@click.option("--abc_results_dir", type=str, required=True)
@click.option("--output_config_name", type=str, default="dataset_config.tsv")
def main(abc_biosamples_config, abc_results_dir, output_config_name):
    biosamples = pd.read_csv(abc_biosamples_config, sep="\t")
    dataset_config = pd.read_csv(CONFIG_TEMPLATE_FILE, sep="\t")
    for i, biosample in biosamples.iterrows():
        biosample_name = biosample["biosample"]
        dataset = {
            "dataset": biosample_name,
            "EnhancerPredictionsAllPutative": os.path.join(
                abc_results_dir,
                biosample_name,
                "Predictions",
                "EnhancerPredictionsAllPutative.tsv.gz",
            ),
            "EnhancerList": os.path.join(
                abc_results_dir,
                biosample_name,
                "Neighborhoods",
                "EnhancerList.txt",
            ),
            "activity": biosample["default_accessibility_feature"],
        }
        dataset_config.loc[i] = dataset

    dataset_config.to_csv(output_config_name, sep="\t", index=False)


if __name__ == "__main__":
    main()
