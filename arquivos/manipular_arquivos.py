import random


class Arquivo:

    def gerar_arquivo(self, tamanho_lista: int) -> list:
        lista_numeros: list = []
        for _ in range(tamanho_lista):
            lista_numeros.append(str(random.randint(-100000, 100000)))
        return lista_numeros

    def salvar_arquivo(self, lista_numeros: list, nome_arquivo: str) -> None:
        with open(f"arquivos/aleatorios/{nome_arquivo}.txt", "w") as arquivo:
            for numero in lista_numeros:
                arquivo.write(numero + "\n")

    def carregar_arquivo(self, nome_arquivo: str) -> list:
        lista_numeros: list = []
        with open(nome_arquivo, "r") as arquivo:
            for linha in arquivo:
                lista_numeros.append(int(linha.strip()))
        return lista_numeros


#
