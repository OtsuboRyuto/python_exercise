import practice06 as p6

if __name__ == '__main__':
    months: list = p6.get_month_name()
    for i in months:
        print(i)

    months.pop(-1)
    print()
    for i in months:
        print(i)
    
        
    