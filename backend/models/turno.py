from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Turno(db.Model):

    __tablename__ = "turnos"

    id = db.Column(db.Integer, primary_key=True)

    numero = db.Column(db.String(20), nullable=False)

    tipo = db.Column(db.String(20), nullable=False)

    condicion = db.Column(db.String(50))

    estado = db.Column(db.String(20), nullable=False)

    fecha_emision = db.Column(db.DateTime)