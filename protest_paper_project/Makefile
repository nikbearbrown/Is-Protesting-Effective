# Simple build for "Is Protesting Effective"
# Usage:
#   make all         # runs data -> figures -> paper
#   make data        # placeholder data processing
#   make figures     # generate all figures
#   make paper       # build paper from Markdown with pandoc (if installed)
#   make clean       # remove derived artifacts

PYTHON=python3

all: data figures paper

data:
	@echo ">> (stub) Data processing step — copy/clean from data_raw -> data_proc"
	$(PYTHON) code/run_all.py --stage data

figures:
	@echo ">> Generating figures"
	$(PYTHON) code/run_all.py --stage figures

paper:
	@echo ">> Building paper (requires pandoc locally)"
	@# Produce both PDF and DOCX if pandoc is available on your machine
	pandoc paper/paper.md -o paper/paper.docx --from markdown --resource-path=.:figures  || echo "pandoc not found; skipping DOCX"
	pandoc paper/paper.md -o paper/paper.pdf  --from markdown --resource-path=.:figures  || echo "pandoc not found; skipping PDF"

clean:
	@echo ">> Cleaning derived files"
	rm -f figures/*.png figures/*.pdf
	rm -f paper/paper.pdf paper/paper.docx
