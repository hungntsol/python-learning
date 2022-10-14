
def merge(arr, left, mid, right):
    L_len = mid - left + 1
    R_len = right - mid

    L = arr[left: left + L_len]
    R = arr[mid + 1: mid + R_len + 1]

    p_left = p_right = 0
    k = left

    while p_left < L_len and p_right < R_len:
        if L[p_left] < R[p_right]:
            arr[k] = L[p_left]
            p_left += 1
        else:
            arr[k] = R[p_right]
            p_right += 1
        k += 1

    while p_left < L_len:
        arr[k] = L[p_left]
        p_left += 1
        k += 1

    while p_right < R_len:
        arr[k] = R[p_right]
        p_right += 1
        k += 1


def merge_sort(arr, left, right):
    if left < right:
        # prevent overflow
        mid = left + (right - left)//2
        # recursive call for the left half
        merge_sort(arr, left, mid)
        # recursive call for the right half
        merge_sort(arr, mid + 1, right)
        # call merge
        merge(arr, left, mid, right)


def solution(arr):
    merge_sort(arr, 0, len(arr) - 1)

    print(arr)


if __name__ == '__main__':
    numbers = list(map(int, input().split()))

    solution(arr=numbers)
