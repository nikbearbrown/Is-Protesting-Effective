# Is Protesting Effective — Buildable Paper Skeleton

This repository provides a reproducible scaffold to build the paper and its figures.

## Structure
- `code/` — one script per figure, plus `utils.py` and `run_all.py`
- `data_raw/` — original datasets (immutable; add your NAVCO, World Bank, etc. here)
- `data_proc/` — processed/cleaned data produced by your ETL
- `figures/` — generated figures (PNG)
- `paper/` — manuscript in Markdown; pandoc used to export DOCX/PDF
- `docs/` — methods appendix and data dictionary (optional)

## Quick Start
```bash
# (optional) create and activate a virtual environment
pip install -r requirements.txt

# Build everything (data -> figures -> paper)
make all

# Or step-by-step
make data
make figures
make paper
```

### Notes
- The current figure scripts are *stubs* that produce placeholder plots so the pipeline runs end-to-end.
- Replace each stub with your analysis (read from `data_proc/` and write to `figures/`).
- `make paper` uses pandoc if available locally to export DOCX/PDF from `paper/paper.md`.
- Keep dataset licenses in mind (e.g., ACLED) and do not commit restricted data.
