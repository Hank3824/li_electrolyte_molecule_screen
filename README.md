# Li Electrolyte Molecule Screening

This repository contains code and curated datasets used for machine-learning-assisted screening of electrolyte solvent and additive candidates for lithium-ion batteries. The workflow combines molecular property prediction, electrostatic-potential descriptors, and hierarchical filtering to enrich candidate molecules for experimental validation.

## Repository Structure

```text
.
|-- data/                   # Curated datasets, annotations, and screening outputs
|-- notebooks/              # English notebooks; record notebooks retain execution outputs
|-- model_artifacts/        # Local Uni-Mol artifact inventory; large weights/SDF ignored
|-- scripts/                # Standalone Python scripts
|-- large_data_not_tracked/ # Local-only large raw files excluded from Git
`-- _original_files/        # Local provenance archive, excluded from Git
```

## Main Datasets

- `data/donor_number.csv`: donor-number dataset for model training.
- `data/esp_344.csv`: ESPmin and ESPmax dataset used for descriptor modelling.
- `data/oxidation_potential.csv`: oxidation-potential dataset.
- `data/pubchem_cleaned_data.csv`: cleaned PubChem-derived molecular library used for screening.
- `data/commercially_available_candidates.csv` and `.xlsx`: commercially available candidate annotations.
- `data/previously_unexplored_candidates.xlsx`: simplified table for previously unexplored candidates, including purchase and experimental-success annotations.
- `data/li_binding_energy_complete.xlsx`: Li+ binding-energy audit dataset.
- `data/kmeans_voronoi_regions.json`: stored K-means/Voronoi region information used for screening visualization.

The raw PubChem export `pubchem.csv` is larger than GitHub's standard single-file limit and is excluded from version control. The cleaned PubChem dataset and curated outputs are included.

## Model Artifacts

The local `model_artifacts/` directory stores Uni-Mol artifact metadata and small cache/configuration files for oxidation-potential, donor-number, ESPmin, and ESPmax prediction. The full local artifact directory is approximately 17 GB. Large `.pth` weight files and `.sdf` structure/cache files are intentionally excluded from ordinary Git tracking because several files exceed GitHub's normal 100 MB single-file limit. The tracked `model_artifacts/README.md` and `model_artifacts/MANIFEST.csv` document the local artifact inventory; uploading the full weight set would require Git LFS or an external model-artifact host.

## Notebooks

- `notebooks/01_data_processing_and_cleaning.ipynb`: PubChem data merging and cleaning workflow.
- `notebooks/02_unimol_dn_esp_training_record.ipynb`: Uni-Mol DN, ESPmin, and ESPmax training record with retained execution outputs.
- `notebooks/03_hierarchical_screening_record.ipynb`: hierarchical screening record with retained execution outputs for OP, DN, ESP, ESPratio, fingerprinting, t-SNE, and K-means assignment.

The two record notebooks retain historical run outputs for provenance. Source cells are standardized in English and use repository-relative paths where practical, including model-artifact paths under `model_artifacts/`. Some historical output logs may still reflect the original execution environment.

## Notes

Predicted oxidation potential, donor number, ESPmin, ESPmax, and ESPratio are screening descriptors. They should be interpreted as candidate-enrichment filters rather than deterministic predictors of final electrochemical performance.
