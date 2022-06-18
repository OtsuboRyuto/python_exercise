def get_month_name() -> list:
    months = ['April', 'May', 'June', 'July', 'August', 'September']
    return months


def contents_of_month(month: str) -> str:
    months = get_month_name()
    if month in months:
        return "存在します"
    else:
        return "存在しません"


if __name__ == '__main__':
    print("月を入力してください ->", end="")
    month = input().capitalize()
    print(contents_of_month(month))
