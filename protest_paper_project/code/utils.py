from pathlib import Path
import matplotlib.pyplot as plt

def ensure_dirs(dirs):
    for d in dirs:
        Path(d).mkdir(parents=True, exist_ok=True)

def savefig(path, fig=None):
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if fig is None:
        plt.savefig(p, dpi=300, bbox_inches="tight")
    else:
        fig.savefig(p, dpi=300, bbox_inches="tight")
    plt.close(fig)

def theme_ax(ax, title=None, xlabel=None, ylabel=None):
    # Clean theme: grid off, readable labels; avoid hard-coded colors
    ax.grid(False)
    if title: ax.set_title(title, fontsize=12)
    if xlabel: ax.set_xlabel(xlabel, fontsize=10)
    if ylabel: ax.set_ylabel(ylabel, fontsize=10)
    for tick in ax.get_xticklabels() + ax.get_yticklabels():
        tick.set_fontsize(9)

def log(msg):
    print(f"[build] {msg}")
