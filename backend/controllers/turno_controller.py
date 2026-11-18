from flask import Blueprint
from flask import jsonify
from flask import request

from services.turno_service import TurnoService

turno_bp = Blueprint(
    "turnos",
    __name__
)

service = TurnoService()


# ---------------------------------
# TURNO REGULAR
# ---------------------------------

@turno_bp.route(
    "/api/turno",
    methods=["POST"]
)
def crear_turno():

    turno = service.crear_turno_regular()

    if not turno:

        return jsonify({
            "mensaje":
            "HORARIO_FINALIZADO"
        })

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

        "personas_delante":
            personas,

        "tiempo_estimado":
            personas * promedio

    })


# ---------------------------------
# TURNO PRIORITARIO
# ---------------------------------

@turno_bp.route(
    "/api/turno-prioritario",
    methods=["POST"]
)
def crear_turno_prioritario():

    datos = request.json

    condicion = datos["condicion"]

    turno = service.crear_turno_prioritario(
        condicion
    )

    if not turno:

        return jsonify({
            "mensaje":
            "HORARIO_FINALIZADO"
        })

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

        "personas_delante":
            personas,

        "tiempo_estimado":
            personas * promedio

    })


# ---------------------------------
# LLAMAR SIGUIENTE
# ---------------------------------

@turno_bp.route(
    "/api/llamar",
    methods=["POST"]
)
def llamar_siguiente():

    turno = service.llamar_siguiente()

    if not turno:

        return jsonify({
            "mensaje":
            "No hay turnos"
        })

    return jsonify({

        "numero": turno.numero,

        "tipo": turno.tipo,

        "condicion": turno.condicion,

        "estado": turno.estado

    })


# ---------------------------------
# INASISTENCIA
# ---------------------------------

@turno_bp.route(
    "/api/inasistencia",
    methods=["POST"]
)
def inasistencia():

    turno = service.marcar_inasistencia()

    if not turno:

        return jsonify({
            "mensaje":
            "No hay turno en atención"
        })

    return jsonify({

        "numero": turno.numero,

        "estado": turno.estado,

        "llamados":
            turno.cantidad_llamados

    })


# ---------------------------------
# PANTALLA TV
# ---------------------------------

@turno_bp.route("/api/pantalla")
def pantalla():

    turno = service.obtener_turno_actual()

    personas = (
        service.obtener_personas_en_espera()
    )

    promedio = (
        service.obtener_tiempo_promedio()
    )

    proximos = (
        service.obtener_proximos_turnos()
    )

    lista_proximos = [
        turno.numero
        for turno in proximos
    ]

    if not turno:

        return jsonify({

            "numero": "---",

            "espera": personas,

            "promedio": promedio,

            "proximos": lista_proximos

        })

    return jsonify({

        "numero": turno.numero,

        "espera": personas,

        "promedio": promedio,

        "proximos": lista_proximos

    })


# ---------------------------------
# FILA DE ESPERA
# ---------------------------------

@turno_bp.route("/api/fila")
def fila():

    fila = service.obtener_fila_espera()

    resultado = []

    for turno in fila:

        resultado.append({

            "numero":
                turno.numero,

            "tipo":
                turno.tipo,

            "estado":
                turno.estado,

            "personas_delante":
                service.obtener_personas_delante(
                    turno.id
                ),

            "llamados":
                turno.cantidad_llamados

        })

    return jsonify(resultado)


# ---------------------------------
# ESTADISTICAS
# ---------------------------------

@turno_bp.route("/api/estadisticas")
def estadisticas():

    return jsonify(
        service.obtener_estadisticas()
    )


# ---------------------------------
# DASHBOARD ADMIN
# ---------------------------------

@turno_bp.route("/api/dashboard")
def dashboard():

    return jsonify(
        service.obtener_dashboard()
    )