# -------------------- IMPORTS --------------------
import os
import pandas as pd
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from xgboost import XGBRegressor
import shap
from matplotlib.ticker import MaxNLocator
from matplotlib import patheffects
from datetime import datetime

# Crear carpeta de figuras si no existe
os.makedirs("figs", exist_ok=True)

# -------------------- ESTILO PRO --------------------
# Fuente: intenta Arial; si no, DejaVu Sans
try:
    mpl.font_manager.findfont("Arial", fallback_to_default=False)
    mpl.rcParams["font.family"] = "Arial"
except Exception:
    mpl.rcParams["font.family"] = "DejaVu Sans"

sns.set_style("whitegrid", {
    "grid.color": "#d0d0d0",
    "grid.linestyle": ":",
    "axes.edgecolor": "#333333"
})
plt.rcParams.update({
    "axes.labelsize": 12,
    "xtick.labelsize": 10.5,
    "ytick.labelsize": 10.5,
    "axes.labelweight": "bold",
    "axes.titleweight": "bold",
    "figure.dpi": 300,
    "savefig.dpi": 300,
})

# Paleta monocroma (olive) con leve gradiente
BASE = np.array(mpl.colors.to_rgb("#6B8E23"))  # olive drab
def lighten(rgb, f):  # f in [0,1]; 0=igual, 1=blanco
    return tuple(rgb + (1 - rgb) * f)

# -------------------- DATOS --------------------
barriers = ['A1','A2','I1','I2','I5','G1','G2','G4','G5','F1','S1','S2']
cross_impact_matrix = np.array([
    [0.00,2.46,1.92,0.00,0.00,0.00,0.00,2.15,2.38,0.00,0.00,0.00],
    [0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,2.31,1.69],
    [1.67,2.17,0.00,0.00,1.75,0.00,0.00,0.00,0.00,0.00,2.17,1.25],
    [2.50,2.50,2.58,0.00,2.25,0.00,0.00,0.00,0.00,0.00,0.00,1.50],
    [1.58,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.33,0.00],
    [2.00,2.00,0.00,0.00,0.00,0.00,0.00,1.58,2.50,2.25,0.00,1.92],
    [0.00,0.00,0.00,1.83,1.58,0.00,0.00,2.00,0.00,0.00,0.00,0.00],
    [2.25,2.25,2.17,2.17,1.92,2.08,1.92,0.00,2.17,0.00,0.00,0.00],
    [2.17,2.42,2.25,0.00,2.25,0.00,2.00,2.17,0.00,0.00,0.00,0.00],
    [0.00,2.67,2.75,2.50,2.36,0.00,0.00,0.00,0.00,0.00,1.45,0.00],
    [0.00,0.00,0.00,1.73,0.00,0.00,0.00,2.18,0.00,0.00,0.00,0.00],
    [0.00,0.00,0.00,0.00,0.00,0.00,0.00,1.82,0.00,0.00,1.73,0.00]
])

# -------------------- MODELO XGBOOST + SHAP --------------------
X_sys = cross_impact_matrix
y_sys = cross_impact_matrix.sum(axis=1)

model_sys = XGBRegressor(n_estimators=150, random_state=42)
model_sys.fit(X_sys, y_sys)

explainer_sys = shap.Explainer(model_sys)
shap_values_sys = explainer_sys(X_sys)

mean_abs_shap = np.abs(shap_values_sys.values).mean(axis=0)

df_shap = pd.DataFrame({'Barrier': barriers, 'SHAP_Value': mean_abs_shap})
df_shap_sorted = df_shap.sort_values(by='SHAP_Value', ascending=True)

# -------------------- GRÁFICO --------------------
fig, ax = plt.subplots(figsize=(7.8, 4.6))

# colores: todos olive; la más alta un poco más oscura
n = len(df_shap_sorted)
cols = [lighten(BASE, 0.35) for _ in range(n)]
cols[-1] = lighten(BASE, 0.15)  # top bar más intensa

bars = ax.barh(
    df_shap_sorted["Barrier"], df_shap_sorted["SHAP_Value"],
    height=0.7,
    color=cols,
    edgecolor="#2b2b2b",
    linewidth=0.6
)

# ejes y grid
for spine in ("top","right"):
    ax.spines[spine].set_visible(False)
ax.spines["left"].set_linewidth(0.7)
ax.spines["bottom"].set_linewidth(0.7)

ax.set_title("Systemic Influence Ranking of Barriers\n(XGBoost + SHAP Analysis)", pad=10)
ax.set_xlabel("Mean Absolute SHAP Value\n(Systemic Influence)")
ax.set_ylabel("Barrier Code")

# ticks agradables
ax.xaxis.set_major_locator(MaxNLocator(nbins=6, prune=None))
ax.xaxis.grid(True)
ax.yaxis.grid(False)

# margen para etiquetas
xmax = df_shap_sorted["SHAP_Value"].max()
ax.set_xlim(0, xmax * 1.16)

# valores al final, con trazo para legibilidad
for b in bars:
    w = b.get_width()
    y = b.get_y() + b.get_height()/2
    txt = ax.text(w + (xmax*0.012), y, f"{w:.3f}", va="center", ha="left", fontsize=10)
    txt.set_path_effects([patheffects.withStroke(linewidth=2, foreground="white", alpha=0.9)])

# pie metodológico discreto
ax.text(0.995, 0.02, "Method: XGBoost + SHAP values",
        transform=ax.transAxes, ha="right", va="bottom", fontsize=9, color="#6f6f6f")

plt.tight_layout(pad=1.0)

# -------------------- EXPORTES --------------------
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
plt.savefig(f"figs/Systemic_Influence_SHAP_Plot_{timestamp}.png", dpi=600, bbox_inches="tight")
plt.savefig(f"figs/Systemic_Influence_SHAP_Plot_{timestamp}.pdf", bbox_inches="tight")
plt.savefig(f"figs/Systemic_Influence_SHAP_Plot_{timestamp}.svg", bbox_inches="tight")
plt.show()

