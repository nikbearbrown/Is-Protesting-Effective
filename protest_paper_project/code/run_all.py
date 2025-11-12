import argparse
import os
from pathlib import Path

from code.utils import ensure_dirs, log

def do_data():
    # Stub: In your real pipeline, read from data_raw and write cleaned joins to data_proc
    ensure_dirs(["data_proc"])
    # Leave a breadcrumb so downstream steps know data stage completed
    (Path("data_proc") / "_DATA_READY.txt").write_text("ok\n")
    log("Data stage complete (stub). Replace with real ETL.")

def do_figures():
    ensure_dirs(["figures"])
    # Call each figure script; a failure in one should not hide others → simple try/excepts
    from code.fig_1 import main as fig1
    from code.fig_2 import main as fig2
    from code.fig_3 import main as fig3
    from code.fig_4 import main as fig4
    from code.fig_5 import main as fig5
    from code.fig_6 import main as fig6
    from code.fig_7 import main as fig7

    for fn, name in [(fig1,"Figure 1"), (fig2,"Figure 2"), (fig3,"Figure 3"),
                     (fig4,"Figure 4"), (fig5,"Figure 5"), (fig6,"Figure 6"), (fig7,"Figure 7")]:
        try:
            fn()
            log(f"{name} OK")
        except Exception as e:
            log(f"{name} FAILED: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--stage", choices=["data","figures","paper","all"], default="all")
    args = parser.parse_args()

    if args.stage in ("data","all"):
        do_data()
    if args.stage in ("figures","all"):
        do_figures()
    # paper stage is handled by Makefile via pandoc; we keep code hook-free here.
