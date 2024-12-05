import multiprocessing
import random

# 2. Napisz równoległą metodę sortowania z wykorzystaniem pakietu multiprocessing


def merge_sorted_arrays(left, right): # łączy 2 posortowane tablice
    arr = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr.append(left[i])
            i += 1
        else:
            arr.append(right[j])
            j += 1

    # dodaje niewykorzystane elementy tablicy
    arr.extend(left[i:])
    arr.extend(right[j:])
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def parallel_selection_sort(arr, process_amount):

    part_size = len(arr) // process_amount
    pool = multiprocessing.Pool(processes=process_amount)
    sorted_parts = pool.map(selection_sort, [arr[i:i + part_size] for i in range(0, len(arr), part_size)])
    pool.close()
    pool.join()

    sorted_arr = sorted_parts[0]
    for part in sorted_parts[1:]:
        sorted_arr = merge_sorted_arrays(sorted_arr, part)
    return sorted_arr


if __name__ == "__main__":
    numbers = []
    N = 20
    for i in range(N):
        numbers.append(random.randint(0, 30))

    print(numbers)

    a = selection_sort(numbers)
    print(a)

    b = parallel_selection_sort(numbers, 3)
    print(b)