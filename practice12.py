import practice06 as p06

if __name__ == '__main__':
    months_list: list = p06.get_month_name()
    print(f"months_list: {months_list}")
    months_list.remove("June")
    
    months_tuple: tuple = tuple(months_list)
    print(f"months_tuple: {months_tuple}")
