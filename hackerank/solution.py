from inspect import _void


def to_string(list):
    return ''.join(list)


def permute(a: list, left: int, right: int) -> _void:
    if left == right:
        print(to_string(a))
    else:
        for i in range(left, right):
            a[left], a[i] = a[i], a[left]
            permute(a, left+1, right)
            a[left], a[i] = a[i], a[left]


if __name__ == "__main__":
    string = "abZs"
    n = len(string)
    a = list(string)
    permute(a, 0, n)
