import random
import pickle


class Arquivo:

    def gerar_arquivo(self, tamanho_lista: int) -> list:
        lista_numeros = random.sample(range(0, 200000), tamanho_lista)
        return lista_numeros

    def salvar_arquivo(self, lista_numeros: list, nome_arquivo: str) -> None:
        with open(f"{nome_arquivo}.txt", "wb") as arquivo:
            pickle.dump(lista_numeros, arquivo)

    def carregar_arquivo(self, nome_arquivo: str) -> list:
        with open(nome_arquivo, "rb") as arquivo:
            return pickle.load(arquivo)
