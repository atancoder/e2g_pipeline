# QC the ABC results
import glob
import gzip
import os
from typing import List

import click
import pandas as pd

MIN_LINE_COUNT = 1e6


def get_prediction_files(abc_results_dir: str) -> List[str]:
    return glob.glob(
        os.path.join(
            abc_results_dir, "*", "Predictions", "EnhancerPredictionsAllPutative.tsv.gz"
        )
    )


def qc_line_count(prediction_files):
    failed_qc_files = {}
    for file_path in prediction_files:
        with gzip.open(file_path, "rt", encoding="utf-8") as file:
            line_count = sum(1 for line in file)
            if line_count < MIN_LINE_COUNT:
                failed_qc_files[file_path] = line_count
    if failed_qc_files:
        raise Exception(
            f"{len(failed_qc_files)} files have < {MIN_LINE_COUNT} lines. Files are: {failed_qc_files}"
        )


@click.command()
@click.option("--abc_results_dir", type=str, required=True)
def main(abc_results_dir):
    prediction_files = get_prediction_files(abc_results_dir)
    qc_line_count(prediction_files)
    print("QC Passed!")


if __name__ == "__main__":
    main()
