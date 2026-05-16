# Li Electrolyte Molecule Screening

This repository contains code and curated datasets used for machine-learning-assisted screening of electrolyte solvent and additive candidates for lithium-ion batteries. The workflow combines molecular property prediction, electrostatic-potential descriptors, and hierarchical filtering to enrich candidate molecules for experimental validation.

## Repository Structure

```text
.
|-- data/                   # Curated datasets and screening outputs
|-- notebooks/              # Cleaned analysis notebooks
|-- scripts/                # Standalone Python scripts
|-- large_data_not_tracked/ # Local-only large raw files excluded from Git
`-- _original_files/        # Local provenance archive, excluded from Git
```

## Main Datasets

- `data/donor_number.csv`: donor-number dataset for model training.
- `data/esp_345.csv`: ESPmin and ESPmax dataset.
- `data/oxidation_potential.csv`: oxidation-potential dataset.
- `data/pubchem_cleaned_data.csv`: cleaned PubChem-derived molecular library used for screening.
- `data/commercially_available_candidates.csv`: cleaned list of 51 commercially available candidates after removing one duplicated or incorrect entry.
- `data/previously_unexplored_candidates_si_table.csv`: simplified SI-style table for 36 previously unexplored commercially available candidates.
- `data/li_binding_energy_complete.xlsx`: Li+ binding-energy audit dataset.

The raw PubChem export `pubchem.csv` is larger than GitHub's standard single-file limit and is excluded from version control. The cleaned PubChem dataset and screening outputs are included.

## Notebooks

- `notebooks/01_data_processing_and_cleaning.ipynb`: PubChem data merging and cleaning workflow.
- `notebooks/02_dn_esp_model_training.ipynb`: donor-number and ESP model training and prediction workflow.
- `notebooks/03_hierarchical_screening.ipynb`: hierarchical candidate-screening workflow.

Notebook outputs were cleared before release to avoid shipping local run logs and machine-specific paths.

## Notes

Predicted oxidation potential, donor number, ESPmin, ESPmax, and ESPratio are screening descriptors. They should be interpreted as candidate-enrichment filters rather than deterministic predictors of final electrochemical performance.
