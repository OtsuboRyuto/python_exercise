# exercise.py - exercise.py
def add(a: int, b: int) -> int:
    """
    Args:
        a (int): first target for adder
        b (int): second target for adder

    Returns:
        int : added result
    """
    return a + b


value1 = int(input("値を入力してください"))
value2 = int(input("値を入力してください"))
print(f"{value1 + value2}")
print(f"{value1 - value2}")
print(f"{add('あ', 2)}")
#! 重要
# *
# ?
