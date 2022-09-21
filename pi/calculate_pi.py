import random


def check_distance_inside(x, y):
    if x**2 + y**2 <= 1:
        return True
    else:
        return False


def calculate_pi(n):
    total_count = 0
    inside_circle = 0

    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if check_distance_inside(x, y):
            inside_circle += 1
        total_count += 1

    return 4 * (inside_circle / total_count)


print(calculate_pi(int(input('n = '))))
