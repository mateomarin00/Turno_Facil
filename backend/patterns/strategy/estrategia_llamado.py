from models.turno import Turno


class EstrategiaLlamado:

    @staticmethod
    def obtener_siguiente():

        prioritario = (
            Turno.query
            .filter_by(
                estado="EN_ESPERA",
                tipo="PRIORITARIO"
            )
            .order_by(Turno.id.asc())
            .first()
        )

        if prioritario:
            return prioritario

        return (
            Turno.query
            .filter_by(
                estado="EN_ESPERA"
            )
            .order_by(Turno.id.asc())
            .first()
        )