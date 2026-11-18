from flask import Blueprint
from flask import jsonify
from flask import request

from services.turno_service import TurnoService


turno_bp = Blueprint(
    "turnos",
    __name__
)

service = TurnoService()


@turno_bp.route(
    "/api/turno",
    methods=["POST"]
)
def crear_turno():

    turno = service.crear_turno_regular()

    personas = (
        service.obtener_personas_delante(
            turno.id
        )
    )

    promedio = (
        service.obtener_tiempo_promedio()
    )

    return jsonify({
        "id": turno.id,
        "numero": turno.numero,
        "tipo": turno.tipo,
        "estado": turno.estado,
        "personas_delante": personas,
        "tiempo_estimado": (
            personas * promedio
        )
    })


@turno_bp.route(
    "/api/turno-prioritario",
    methods=["POST"]
)
def crear_turno_prioritario():

    datos = request.get_json()

    condicion = datos["condicion"]

    turno = service.crear_turno_prioritario(
        condicion
    )

    personas = (
        service.obtener_personas_delante(
            turno.id
        )
    )

    promedio = (
        service.obtener_tiempo_promedio()
    )

    return jsonify({
        "id": turno.id,
        "numero": turno.numero,
        "tipo": turno.tipo,
        "condicion": turno.condicion,
        "estado": turno.estado,
        "personas_delante": personas,
        "tiempo_estimado": (
            personas * promedio
        )
    })


@turno_bp.route(
    "/api/llamar",
    methods=["POST"]
)
def llamar_siguiente():

    turno = service.llamar_siguiente()

    if not turno:

        return jsonify({
            "mensaje": "No hay turnos"
        })

    return jsonify({
        "numero": turno.numero,
        "tipo": turno.tipo,
        "condicion": turno.condicion,
        "estado": turno.estado
    })


@turno_bp.route(
    "/api/inasistencia",
    methods=["POST"]
)
def inasistencia():

    turno = service.marcar_inasistencia()

    if not turno:

        return jsonify({
            "mensaje": "No hay turno en atención"
        })

    return jsonify({
        "numero": turno.numero,
        "estado": turno.estado
    })


@turno_bp.route("/api/pantalla")
def pantalla():

    turno = (
        service.obtener_turno_actual()
    )

    personas = (
        service.obtener_personas_en_espera()
    )

    promedio = (
        service.obtener_tiempo_promedio()
    )

    if not turno:

        return jsonify({
            "numero": "---",
            "espera": personas,
            "promedio": promedio
        })

    return jsonify({
        "numero": turno.numero,
        "espera": personas,
        "promedio": promedio
    })


@turno_bp.route("/api/fila")
def fila():

    fila = service.obtener_fila_espera()

    resultado = []

    for turno in fila:

        resultado.append({
            "numero": turno.numero,
            "tipo": turno.tipo,
            "estado": turno.estado,
            "personas_delante":
                service.obtener_personas_delante(
                    turno.id
                )
        })

    return jsonify(resultado)


@turno_bp.route("/api/estadisticas")
def estadisticas():

    return jsonify(
        service.obtener_estadisticas()
    )


@turno_bp.route("/api/dashboard")
def dashboard():

    return jsonify(
        service.obtener_dashboard()
    )