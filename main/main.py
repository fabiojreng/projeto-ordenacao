import openpyxl
import time
from sort.radix_sort import RadixSort
from sort.comb_sort import CombSort
import os
import sys

sys.path.insert(0, os.path.abspath(os.curdir))
from arquivos.manipular_arquivos import Arquivo

arquivo = Arquivo()
radix_sort = RadixSort()
comb_sort = CombSort()


def calcular_tempo_radix(lista: list) -> float:
    inicio = time.time()
    radix_sort.radixSort(lista)
    fim = time.time()
    return fim - inicio


def calcular_tempo_comb(lista: list) -> float:
    inicio = time.time()
    comb_sort.comb_sort(lista)
    fim = time.time()
    return fim - inicio


lista_radix_sort: list = [
    arquivo.carregar_arquivo(f"./arquivos/positivos/lista{i}Mil.txt")
    for i in range(10, 151, 10)
]

lista_comb_sort: list = [
    arquivo.carregar_arquivo(f"./arquivos/aleatorios/lista{i}Mil.txt")
    for i in range(10, 151, 10)
]

with open("resultados_radix_sort.txt", "a") as arquivo:
    for index, lista in enumerate(lista_radix_sort, start=1):
        arquivo.write(f"Tempo para a lista {index}: {calcular_tempo_radix(lista)}\n")

with open("resultados_comb_sort.txt", "w") as arquivo:
    for index, lista in enumerate(lista_comb_sort, start=1):
        arquivo.write(f"Tempo para a lista {index}: {calcular_tempo_comb(lista)}\n")


wb = openpyxl.Workbook()

ws1 = wb.active
ws1.title = "Radix Sort"


for i in range(1, 16):
    ws1.cell(row=1, column=i, value=f"Lista {i * 10000}")

for i in range(30):
    for index, lista in enumerate(lista_radix_sort, start=1):
        tempo = calcular_tempo_radix(lista)
        ws1.cell(row=i + 2, column=index, value=tempo)

print("Finalizado")

ws2 = wb.create_sheet(title="Comb Sort")

for i in range(1, 16):
    ws2.cell(row=1, column=i, value=f"Lista {i * 10000}")

for i in range(30):
    for index, lista in enumerate(lista_comb_sort, start=1):
        tempo = calcular_tempo_comb(lista)
        ws2.cell(row=i + 2, column=index, value=tempo)

wb.save("resultados.xlsx")
print("Finalizado")
