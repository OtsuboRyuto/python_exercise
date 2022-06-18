def is_natural(n: int) -> bool:
    if n < 0:
        return False
    else:
        return True


if __name__ == '__main__':
    print("数値を入力してください ->", end="")
    value1 = input()
    try:
        value1 = int(value1)
    except:
        exit()

    if is_natural(value1):
        print("自然数です")
    else:
        print("自然数ではありません")
