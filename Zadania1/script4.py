import random

# - Napisz skrypt sortujący liczby (dwoma wybranymi metodami). Wygeneruj losowo N liczb - wykorzystaj standardową funkcję do losowania. Z wbudowanej funkcji sortującej korzystaj tylko w celu weryfikacji wyników.


def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    numbers = []
    N = 20
    for i in range(N):
        numbers.append(random.randint(0, 30))

    print(numbers)
    print(bubble_sort(numbers))
    print(selection_sort(numbers))

    numbers.sort()
    print(numbers)
