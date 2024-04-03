class CombSort:

    def comb_sort(self, array: list) -> list:
        gap = len(array)
        shrink_factor = 1.3
        sorted = False

        while not sorted:
            gap = int(gap / shrink_factor)
            if gap <= 1:
                gap = 1
                sorted = True

            i = 0
            while i + gap < len(array):
                if array[i] > array[i + gap]:
                    array[i], array[i + gap] = array[i + gap], array[i]
                    sorted = False
                i += 1

        return array
