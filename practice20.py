def add(*args: int) -> int:
    """
    Args:
        args (int): target for adder
    Returns:
        int : added result
    """
    return sum(args)


if __name__ == '__main__':
    print("数値を入力してください -> ", end="")
    t: int = int(input())
    for i in range(4):
        if i == 0:
            print(f"引数なし= {add()}")
        else:
            print(f"引数{i}\t= {add(*[t for x in range(i)])}")
