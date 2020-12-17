
def min_step(x, y):
    if x == y:
        return 0

    if x > y:
        return x - y

    if y % 2 == 1:
        return 1 + min_step(x, y + 1)
    else:
        return 1 + min_step(x, y / 2)


if __name__ == '__main__':
    x = 6
    y = 8
    print("min steps :", min_step(x, y))
