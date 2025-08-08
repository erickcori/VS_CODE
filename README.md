# SHAP Systemic Influence Plot

Genera un ranking de barreras utilizando **XGBoost** + **SHAP**, con exportación automática de gráficos en alta resolución (PNG, PDF y SVG en la carpeta `figs/`).

## 📦 Requisitos

Instalar las dependencias con:

```bash
pip install -r requirements.txt

▶️ Uso
Ejecutar el script principal:
python plot_shap.py
Esto generará las figuras en figs/ con resolución de 600 dpi.

📂 Estructura del proyecto
bash
Copiar
Editar
VS_CODE/
│-- plot_shap.py           # Script principal
│-- requirements.txt       # Dependencias
│-- README.md              # Documentación
│-- .gitignore             # Archivos ignorados por Git
└── figs/                   # Salida de figuras (ignorada por Git)

📜 Licencia
MIT License

Si quieres, te lo preparo ya listo para **copiar y pegar** en tu `README.md` y hacer el **Commit → Push**, así tu repo queda con un README de nivel Q1 😏.  

¿Quieres que lo haga ahora?
