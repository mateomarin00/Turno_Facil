class SecuenciadorTurnos:

    _instancia = None
    contador = 1

    def __new__(cls):

        if cls._instancia is None:
            cls._instancia = super().__new__(cls)

        return cls._instancia

    def generar_numero(self):

        numero = f"P-{self.contador:03d}"

        self.contador += 1

        return numero