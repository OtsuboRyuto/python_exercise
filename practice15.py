from calendar import month
import practice13 as p13

if __name__ == '__main__':
    months: dict = p13.get_month_name()
    p13.show_dict(months)
    print()
    months.update({"October": 31})
    p13.show_dict(months)
