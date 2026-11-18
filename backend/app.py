from flask import Flask, render_template
from flask_cors import CORS

from config import Config
from models.turno import db, Turno
from controllers.turno_controller import turno_bp

app = Flask(
    __name__,
    template_folder="../frontend/templates",
    static_folder="../frontend/static"
)

CORS(app)

app.config.from_object(Config)

db.init_app(app)

app.register_blueprint(turno_bp)


# ----------------------------
# Vistas principales
# ----------------------------

@app.route("/")
def inicio():
    return "TurnoFacil funcionando"


@app.route("/kiosco")
def kiosco():
    return render_template("kiosco.html")


@app.route("/asesor")
def asesor():
    return render_template("asesor.html")


@app.route("/pantalla")
def pantalla():
    return render_template("pantalla.html")


@app.route("/condicion-especial")
def condicion_especial():
    return render_template("condicion_especial.html")


@app.route("/turno-emitido")
def turno_emitido():
    return render_template("turno_emitido.html")


@app.route("/admin")
def administrador():
    return render_template("administrador.html")


# ----------------------------
# Inicialización de BD
# ----------------------------

with app.app_context():

    db.create_all()

    # Limpia datos anteriores para iniciar
    # cada demostración desde cero
    Turno.query.delete()

    db.session.commit()


# ----------------------------
# Inicio aplicación
# ----------------------------

if __name__ == "__main__":
    app.run(debug=True)