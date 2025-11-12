import matplotlib.pyplot as plt
import numpy as np
from .utils import savefig, theme_ax

def main():
    x = np.arange(1, 6)
    y = np.linspace(0.2, 0.8, 5)
    fig, ax = plt.subplots(figsize=(6.5, 3.5))
    ax.plot(x, y, marker='o')
    theme_ax(ax, title="Figure 5: Media Framing Effects (Stub)", xlabel="Category", ylabel="Share")
    savefig("figures/fig5_media_stub.png", fig)
