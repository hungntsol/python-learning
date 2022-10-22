def solution(res, cmd, args):
    if cmd != "print":
        join_args = ",".join(args)
        cmd += f"({join_args})"
        eval("res." + cmd)
    else:
        print(res)

    return res


if __name__ == "__main__":
    n = int(input())
    exec_commands = []

    res = []

    for i in range(0, n):
        command, *args = input().split()
        res = solution(res, command, args)

    print(res)
