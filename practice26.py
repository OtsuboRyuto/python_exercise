from dataclasses import dataclass
import practice25 as p25
import dataclasses
import util as ut


# @dataclasses.dataclass
class Card:
    #user_name: str
    #point: int = 0
    def __init__(self, user_name: str):
        self.user_name: str = user_name
        self.point: int = 0

    def add_point(self, point: int) -> None:
        self.point += point


if __name__ == '__main__':
    print("カードの所有者名を入力してください -> ", end="")
    name: str = input()
    c: Card = Card(name)
    print(f"{c.user_name}\n{c.point}")
    print("追加ポイントを入力してください -> ", end="")
    point: int = ut.input_int()
    c.add_point(point)
    # print(f"{c.user_name}\n{c.point}")
    for i in c.__dict__:
        print(i)
