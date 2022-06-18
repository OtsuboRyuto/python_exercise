import practice06 as p6

if __name__ == '__main__':
    months: list = p6.get_month_name()
    months.append("October")
    for i in months:
        print(i)
