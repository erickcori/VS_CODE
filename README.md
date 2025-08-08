# SHAP Systemic Influence Plot

Genera un ranking de barreras utilizando **XGBoost** + **SHAP**, con exportación automática de gráficos en alta resolución (PNG, PDF y SVG) en la carpeta `figs/`.

---

## 📋 Requisitos

Instalar las dependencias con:
pip install -r requirements.txt

▶ Uso
Ejecutar el script principal:

bash
Copiar
Editar
python plot_shap.py
Esto generará las figuras en figs/ con resolución de 600 dpi, en formatos PNG, PDF y SVG.

📂 Estructura del proyecto
bash
Copiar
Editar
VS_CODE/
│-- plot_shap.py       # Script principal
│-- requirements.txt   # Dependencias
│-- README.md          # Documentación
│-- .gitignore         # Archivos ignorados por Git
│-- figs/              # Salida de figuras (ignoradas por Git)

##📄 Licencia
MIT License

##💡 Notas
La carpeta figs/ está incluida en .gitignore para no subir las imágenes generadas.

Puedes modificar el script plot_shap.py para ajustar colores, títulos o formato de exportación.

## 🔄 Flujo recomendado para subir cambios a GitHub
Guardar los cambios.

Stage All (icono ➕ en el panel Git de VS Code).

Escribir un mensaje breve (ej: feat: add high-res SHAP plots).

Commit (✓).

Push (flecha ↑ o “Sync Changes”).
