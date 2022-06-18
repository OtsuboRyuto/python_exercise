def add(a: int, b: int) -> int:
    """
    Args:
        a (int): first target for adder
        b (int): second target for adder

    Returns:
        int : added result
    """
    return a + b


if __name__ == '__main__':
    print("数値1を入力してください -> ", end="")
    try:
        a: int = int(input())
    except:
        exit()

    print("数値2を入力してください -> ", end="")
    try:
        b: int = int(input())
    except:
        exit()
    print(f"{add(a, b)}")
