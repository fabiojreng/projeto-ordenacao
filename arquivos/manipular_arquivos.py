import random


class Arquivo:
    @staticmethod
    def gerar_arquivo(tamanho_lista: int) -> list:
        lista_numeros: list = []
        for _ in range(tamanho_lista):
            lista_numeros.append(str(random.randint(-100000, 100000)))
        return lista_numeros

    @staticmethod
    def salvar_arquivo(lista_numeros: list, nome_arquivo: str) -> None:
        with open(f"{nome_arquivo}.txt", "w") as arquivo:
            for numero in lista_numeros:
                arquivo.write(numero + "\n")

    @staticmethod
    def carregar_arquivo(nome_arquivo: str) -> list:
        lista_numeros: list = []
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                lista_numeros.append(int(linha.strip()))
        return lista_numeros

    @classmethod
    def carregar_listas(cls, caminho_arquivo: str) -> list:
        lista_sort: list = [
            cls.carregar_arquivo(f"{caminho_arquivo}lista{i}Mil.txt")
            for i in range(10, 151, 10)
        ]
        return lista_sort
