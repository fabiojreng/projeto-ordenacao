import time


class CalcularTempo:
    @staticmethod
    def calcular_tempo(algoritmo, lista: list) -> float:
        inicio = time.time()
        algoritmo(lista)
        fim = time.time()
        return fim - inicio
