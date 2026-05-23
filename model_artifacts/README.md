# Model Artifacts

This directory stores local Uni-Mol model artifacts used by the notebooks in this repository. It contains the trained weights for oxidation-potential, donor-number, ESPmin, and ESPmax models, together with Uni-Mol generated structure/cache files used during prediction and training.

Large `.pth` weight files and `.sdf` structure/cache files are intentionally excluded from ordinary Git tracking because several files exceed GitHub's normal 100 MB single-file limit. Small Uni-Mol cache/configuration files (`.yaml`, `.ss`, `.data`, and `.result`) are tracked together with `MANIFEST.csv` for provenance. Uploading the full weight set would require Git LFS or an external model-artifact host.

## Local Inventory

- Total files: 1160
- Total size: 17006.60 MB
- Largest file: `Oxidation Potential/model_0.pth` (626.27 MB)

## Top-Level Contents

- `Donor Number/`: 37 files, 3394.38 MB
- `ESP/`: 87 files, 6342.11 MB
- `Oxidation Potential/`: 1036 files, 7270.11 MB

## File Types

- `.pth`: 53 files, 11801.18 MB
- `.sdf`: 1063 files, 5204.81 MB
- `.data`: 11 files, 0.59 MB
- `.ss`: 11 files, 0.01 MB
- `.yaml`: 11 files, 0.01 MB
- `.result`: 11 files, 0.00 MB

## Usage

The record notebooks refer to this directory through repository-relative paths. When reproducing the workflow locally, keep this folder at the repository root as `model_artifacts/`.
