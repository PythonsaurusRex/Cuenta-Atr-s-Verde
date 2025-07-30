# Importa las herramientas necesarias de Flask
from flask import Flask, render_template, request, redirect, url_for

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Lista vacía donde se guardan las ideas de los usuarios
ideas = []

# Ruta de la página principal
@app.route("/")
def index():
    return render_template("index.html")

# Ruta que muestra las recomendaciones para cuidar el planeta
@app.route("/recomendaciones")
def recomendaciones():
    return render_template("recomendaciones.html")

# Ruta donde se muestran las ideas y se permite agregarlas
@app.route("/ideas", methods=["GET", "POST"])
def ideas_page():
    if request.method == "POST":
        # Toma el valor que el usuario escribió en el formulario
        nueva_idea = request.form.get("idea")
        if nueva_idea:
            ideas.append(nueva_idea) # Agrega la idea a la lista
        return redirect(url_for("ideas_page")) # Redirige para actualizar
    
    # Si se pasa un parámetro de eliminar, borra la idea correspondiente
    eliminar = request.args.get("eliminar")
    if eliminar and eliminar in ideas:
        ideas.remove(eliminar)
    return render_template("ideas.html", ideas=ideas)

# Inicia la app en modo debug (solo para desarrollo)
if __name__ == "__main__":
    app.run(debug=True)
