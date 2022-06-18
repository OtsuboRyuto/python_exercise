def is_multiple(n, m) -> bool:
    return n % m == 0


def is_multiple_of_4(n: int) -> bool:
    return is_multiple(n, 4)


if __name__ == '__main__':
    print("数値を入力してください ->", end="")
    value1 = input()
    try:
        value1 = int(value1)
    except:
        exit()
    if is_multiple_of_4(value1):
        print("4の倍数です")
    else:
        print("4の倍数ではありません")
