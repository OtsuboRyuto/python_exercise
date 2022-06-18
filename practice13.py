def get_month_name() -> dict:
    return {"April": 31, "May": 31, "June": 30, "July": 31, "August": 31, "September": 30}


def show_dict(d: dict) -> None:
    for key, value in d.items():
        print(key, value)


if __name__ == '__main__':
    months: dict = get_month_name()
    show_dict(months)
