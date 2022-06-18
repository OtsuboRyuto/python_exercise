from dataclasses import dataclass


@dataclass
class input_class:
    price: int
    tax_rate: float

    def calculate_tax(self) -> int:
        tax = self.price * self.tax_rate
        return int(tax)


if __name__ == '__main__':
    data: input_class = input_class(price=100, tax_rate=1.08)
    print("単価を入力してください -> ", end="")
    x: int = input()
    if x != "":
        try:
            data.price = int(x)
        except ValueError:
            print("数値を入力してください")
            exit()
    print("税率(%)を入力してください -> ", end="")
    y: float = input()
    if y != "":
        try:
            data.tax_rate = float(y)
        except ValueError:
            print("数値を入力してください")
            exit()

    print(f"税込価格 : {data.calculate_tax()}")
