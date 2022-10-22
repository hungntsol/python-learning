
def solution(arr):
    dp = [0] * len(arr)

    dp[0] = 1

    for i in range(0, len(arr)):
        for j in range(0, i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))


if __name__ == "__main__":
    numbers = list(map(int, input().split()))
    solution(numbers)
