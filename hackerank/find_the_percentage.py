from statistics import mean


def solution(student_marks, query_name):
    print("{:.2f}".format(mean(student_marks[query_name])))


if __name__ == "__main__":
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()

    solution(student_marks, query_name)
