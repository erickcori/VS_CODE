# SHAP Systemic Influence Plot

Generates a ranking of systemic barriers using **XGBoost + SHAP**, exporting high-resolution figures (PNG, PDF, and SVG) to the `figs/` folder.

---

## 📋 Requirements

Install the dependencies:

```bash
pip install -r requirements.txt

▶ Usage
Run the main script:

python plot_shap.py

This will generate figures in figs/ at 600 dpi in PNG, PDF, and SVG formats.

📂 Project Structure

VS_CODE/
│-- plot_shap.py       # Main script
│-- requirements.txt   # Dependencies
│-- README.md          # Documentation
│-- .gitignore         # Files ignored by Git
│-- figs/              # Figure outputs (ignored by Git)

📄 License
MIT License

💡 Notes
The figs/ folder is listed in .gitignore so generated images are not committed.

You can tweak plot_shap.py to adjust colors, titles, or export settings.


🔄 Recommended Git Workflow
Save your changes.

Stage All (➕ icon in VS Code’s Source Control).

Write a short message (e.g., feat: add high-res SHAP plots).

Commit (✓).

Push (↑ or “Sync Changes”).

