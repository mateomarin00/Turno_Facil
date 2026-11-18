from .turno_factory import TurnoFactory

class TurnoPrioritarioFactory(TurnoFactory):

    def crear_turno(self):

        return {
            "tipo": "PRIORITARIO"
        }