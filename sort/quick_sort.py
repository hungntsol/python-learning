def swap_arr(arr, i, j):
    (arr[i], arr[j]) = (arr[j], arr[i])


def partition(arr, low, hight):
    pivot = arr[hight]

    p_greater = low - 1

    for i in range(low, hight):
        if arr[i] <= pivot:
            p_greater += 1

            swap_arr(arr, p_greater, i)

    swap_arr(arr, p_greater + 1, hight)

    return p_greater + 1


def quick_sort(arr, low, hight):
    if low < hight:
        pivot = partition(arr, low, hight)

        quick_sort(arr, low, pivot - 1)
        quick_sort(arr, pivot + 1, hight)


def solution(arr):
    quick_sort(arr, 0, len(arr) - 1)

    print(arr)


if __name__ == '__main__':
    numbers = list(map(int, input().split()))

    solution(numbers)
