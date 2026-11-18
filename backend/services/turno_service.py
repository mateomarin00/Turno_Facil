from datetime import datetime

from models.turno import Turno
from models.turno import db

from patterns.strategy.estrategia_llamado import (
    EstrategiaLlamado
)

from patterns.singleton.secuenciador import (
    SecuenciadorTurnos
)


class TurnoService:

    def crear_turno_regular(self):

        if not self.horario_habilitado():
            return None
        

        secuenciador = SecuenciadorTurnos()

        numero = secuenciador.generar_numero()

        turno = Turno(
            numero=numero,
            tipo="REGULAR",
            estado="EN_ESPERA",
            fecha_emision=datetime.now()
        )

        db.session.add(turno)
        db.session.commit()

        return turno

    def crear_turno_prioritario(
        self,
        condicion
    ):
        if not self.horario_habilitado():
            return None
        secuenciador = SecuenciadorTurnos()

        numero = secuenciador.generar_numero()

        turno = Turno(
            numero=numero,
            tipo="PRIORITARIO",
            condicion=condicion,
            estado="EN_ESPERA",
            fecha_emision=datetime.now()
        )

        db.session.add(turno)
        db.session.commit()

        return turno

    def llamar_siguiente(self):

        turno = (
            EstrategiaLlamado
            .obtener_siguiente()
        )

        if not turno:
            return None

        turno.estado = "EN_ATENCION"

        db.session.commit()

        return turno

    def marcar_inasistencia(self):

        turno = (
            Turno.query
            .filter_by(
                estado="EN_ATENCION"
            )
            .order_by(
                Turno.id.desc()
            )
            .first()
        )

        if not turno:
            return None

        turno.cantidad_llamados += 1

        if turno.cantidad_llamados >= 3:

            turno.estado = "CANCELADO"

        else:

            turno.estado = "EN_ESPERA"

        db.session.commit()

        return turno

    def obtener_turno_actual(self):

        return (
            Turno.query
            .filter_by(
                estado="EN_ATENCION"
            )
            .order_by(
                Turno.id.desc()
            )
            .first()
        )

    def obtener_personas_en_espera(self):

        return (
            Turno.query
            .filter_by(
                estado="EN_ESPERA"
            )
            .count()
        )

    def obtener_tiempo_promedio(self):

        return 3

    def obtener_tiempo_total_espera(self):

        return (
            self.obtener_personas_en_espera()
            *
            self.obtener_tiempo_promedio()
        )

    def obtener_personas_delante(
        self,
        turno_id
    ):

        turno_actual = Turno.query.get(
            turno_id
        )

        return (
            Turno.query
            .filter(
                Turno.id < turno_actual.id,
                Turno.estado == "EN_ESPERA"
            )
            .count()
        )

    def obtener_fila_espera(self):

        return (
            Turno.query
            .filter_by(
                estado="EN_ESPERA"
            )
            .order_by(
                Turno.id.asc()
            )
            .all()
        )

    def obtener_proximos_turnos(self):

        turnos = (
            Turno.query
            .filter_by(
                estado="EN_ESPERA"
            )
            .order_by(
                Turno.id.asc()
            )
            .limit(3)
            .all()
    )

        return turnos

    def obtener_estadisticas(self):

        espera = (
            Turno.query
            .filter_by(
                estado="EN_ESPERA"
            )
            .count()
        )

        prioritarios = (
            Turno.query
            .filter_by(
                estado="EN_ESPERA",
                tipo="PRIORITARIO"
            )
            .count()
        )

        regulares = (
            Turno.query
            .filter_by(
                estado="EN_ESPERA",
                tipo="REGULAR"
            )
            .count()
        )

        return {
            "espera": espera,
            "prioritarios": prioritarios,
            "regulares": regulares,
            "tiempo_total":
                self.obtener_tiempo_total_espera()
        }

    def obtener_dashboard(self):

        emitidos = Turno.query.count()

        espera = (
            Turno.query
            .filter_by(
                estado="EN_ESPERA"
            )
            .count()
        )

        atencion = (
            Turno.query
            .filter_by(
                estado="EN_ATENCION"
            )
            .count()
        )

        cancelados = (
            Turno.query
            .filter_by(
                estado="CANCELADO"
            )
            .count()
        )

        prioritarios = (
            Turno.query
            .filter_by(
                tipo="PRIORITARIO"
            )
            .count()
        )

        regulares = (
            Turno.query
            .filter_by(
                tipo="REGULAR"
            )
            .count()
        )

        return {
            "emitidos": emitidos,
            "espera": espera,
            "atencion": atencion,
            "cancelados": cancelados,
            "prioritarios": prioritarios,
            "regulares": regulares,
            "promedio": 3,
            "tiempo_total":
                self.obtener_tiempo_total_espera()
        }

    def horario_habilitado(self):

        hora_actual = datetime.now()

        hora_limite = hora_actual.replace(
            hour=19,
            minute=45,
            second=0,
            microsecond=0
        )

        return hora_actual < hora_limite