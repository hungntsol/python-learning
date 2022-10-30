from re import sub


def count_substring(string, sub_string):
    result = 0

    for i in range(0, len(string)):
        if string[i] == sub_string[0]:
            if string[i:len(sub_string) + 1] == sub_string:
                result += 1
                i += len(sub_string)

    return result


if __name__ == "__main__":
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
