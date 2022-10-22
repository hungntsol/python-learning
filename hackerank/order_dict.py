from collections import OrderedDict


if __name__ == "__main__":
    n = int(input())

    cart_items = OrderedDict()

    for _ in range(0, n):
        item, price = input().split()
        cart_items[item] = cart_items.get(item, 0) + int(price)

    for k, v in cart_items.items():
        print(k, v)
