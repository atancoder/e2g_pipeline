# QC the ABC results
import glob
import os
from typing import List

import click

MIN_FILE_SIZE_MB = 10


def get_prediction_files(abc_results_dir: str) -> List[str]:
    return glob.glob(
        os.path.join(
            abc_results_dir, "*", "Predictions", "EnhancerPredictionsAllPutative.tsv.gz"
        )
    )


def qc_line_count(prediction_files):
    failed_qc_files = {}
    for file_path in prediction_files:
        size_mb = int(os.path.getsize(file_path) / 1e6)
        if size_mb < MIN_FILE_SIZE_MB:
            failed_qc_files[file_path] = size_mb
    if failed_qc_files:
        raise Exception(
            f"{len(failed_qc_files)} files have < {MIN_FILE_SIZE_MB} MB. Files are: {failed_qc_files}"
        )


@click.command()
@click.option("--abc_results_dir", type=str, required=True)
def main(abc_results_dir):
    prediction_files = get_prediction_files(abc_results_dir)
    qc_line_count(prediction_files)
    print("QC Passed!")


if __name__ == "__main__":
    main()
