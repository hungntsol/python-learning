def swap_case(s):
    return "".join([letter.upper() if letter.islower() else letter.lower() for letter in s])


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
