from .turno_factory import TurnoFactory

class TurnoRegularFactory(TurnoFactory):

    def crear_turno(self):

        return {
            "tipo": "REGULAR"
        }