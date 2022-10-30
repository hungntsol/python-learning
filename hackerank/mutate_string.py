def mutate_string(string, position, character):
    l = list(string)
    print(l)
    return "".join(l)


if __name__ == "__main__":
    string = input()
    position, character = input().split()
    s = mutate_string(string, int(position), character)
    print(s)
