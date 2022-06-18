def display_multiple_of_six(start : int, end : int) -> None:
    """_summary_

    Args:
        start (int): _description_
        end (int): _description_
    """
    for i in range(start, end + 1):
        if i % 6 == 0:
            print(i)


if __name__ == '__main__':
    start = 24
    end = 100
    display_multiple_of_six(start, end)
    