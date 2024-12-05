from script2 import merge_sorted_arrays, selection_sort, parallel_selection_sort
import multiprocessing
import random
import time
import matplotlib.pyplot as plt

# 3. Uruchom testy metody z pktu 2 z różnymi rozmiarami danych wejściowych oraz różną liczbą procesów, następnie przedstaw zebrane wyniki w postaci graficznej z użyciem matplotlib.


def run_tests():
    sizes = [1000, 5000, 10000, 20000, 40000]  # rozmiary tablic
    process_list = [1, 2, 4, 8]  # ilości procesów
    results = {}

    for size in sizes:
        arr = [random.randint(0, 50000) for _ in range(size)]
        results[size] = []

        for process_num in process_list:
            start_time = time.time()
            parallel_selection_sort(arr, process_num)
            elapsed_time = time.time() - start_time
            results[size].append(elapsed_time)

    return results, sizes, processes_list


def plot_results(results, sizes, processes_list):
    plt.figure(figsize=(10, 6))

    for num_processes in processes_list:
        times = [results[size][processes_list.index(num_processes)] for size in sizes]
        plt.plot(sizes, times, label=f'{num_processes} procesów', marker='o')

    plt.title('Czas sortowania równoległego zależny od rozmiaru danych i liczby procesów')
    plt.xlabel('Rozmiar danych')
    plt.ylabel('Czas wykonania (sekundy)')
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":

    results, sizes, processes_list = run_tests()

    plot_results(results, sizes, processes_list)