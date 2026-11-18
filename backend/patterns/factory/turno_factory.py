from abc import ABC, abstractmethod

class TurnoFactory(ABC):

    @abstractmethod
    def crear_turno(self):
        pass