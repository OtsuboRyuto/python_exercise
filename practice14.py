import practice13 as p13


def contains_dict_value(d: dict, key: str) -> bool:
    return key in d


def contains_dict_key(d: dict, value: str) -> bool:
    return value in d.keys()


if __name__ == '__main__':
    print("月を入力してください ->", end="")
    month: str = str.capitalize(input())
    months: dict = p13.get_month_name()
    if contains_dict_key(months, month):
        print(f"{months.get(month)}")
    else:
        print("存在しません")
