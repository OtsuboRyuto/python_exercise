import practice26 as p26


class Card(p26.Card):
    @staticmethod
    def calc_point(rate: float, point: int) -> int:
        return int(point * rate)

    def show_detail(self) -> None:
        print(f"{self.user_name}\n{self.point}")


if __name__ == '__main__':
    print("カードの所有者名を入力してください -> ", end="")
    n = input()
    card: Card = Card(n)
    print("計算したいポイントを教えてください -> ", end="")
    p = int(input())
    print("計算したい倍率を教えてください -> ", end="")
    r = float(input())
    print(f"{card.calc_point(r, p)}")
    card.show_detail()
