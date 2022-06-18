from typing import Final, final


from collections.abc import Callable


def calculate_adults(people: int) -> Callable:
    def sum_price(default=1000):
        return people * default
    return sum_price


def calculate_children(people: int) -> Callable:
    def sum_price(default=800):
        return people * default
    return sum_price


if __name__ == '__main__':
    print("大人の人数を入力してください -> ", end="")
    adults: Final[int] = int(input())
    sum_adults = calculate_adults(adults)
    print("子供の人数を入力してください -> ", end="")
    children: Final[int] = int(input())
    sum_children = calculate_children(children)
    print(f"大人料金合計 : {sum_adults()}")
    print(f"子供料金合計 : {sum_children()}")
