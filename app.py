from flask import Flask
from data.data_productos import productos, categorias

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def home():
        nombre = "Franco Moreira"
        descripcion = "Soy estudiante de la tecnicatura de Desarrollo Web y me encuentro realizando la materia de Programacion Web Dinamica :) ."
        return f"Hola! como va? Soy {nombre}. {descripcion}"

    @app.route("/productos")
    def listar_productos():
        salida = ""
        for p in productos:
            salida += f"ID: {p['id']} - Descripción: {p['descripcion']} - Categoría ID: {p['categoria_id']}<br>"
        return salida

    @app.route("/categorias")
    def listar_categorias():
        salida = ""
        for c in categorias:
            salida += f"ID: {c['id']} - Descripción: {c['descripcion']}<br>"
        return salida

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
