from manipular_excel import ManipularExcel
from sort.comb_sort import CombSort
from sort.radix_sort import RadixSort


class Main:
    def __init__(self):
        self.radix_sort = RadixSort()
        self.comb_sort = CombSort()
        self.excel = ManipularExcel()

    def run(self):
        self.excel.execute_radix(self.radix_sort.radixSort)
        self.excel.execute_comb(self.comb_sort.comb_sort)
        self.excel.salvar("resultados.xlsx")


main_sort = Main()
main_sort.run()
