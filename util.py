import typing
import re


def int_validate(func: typing.Callable) -> typing.Callable:
    def int_validate_inner(*args: int) -> str:
        t = func(*args)
        if t == "" or (re.match(r"[0-9]+", t) == None):
            print("整数で入力してください")
            #raise Exception("整数で入力してください")
            exit()
        return t
    return int_validate_inner


@int_validate
def input2() -> str:
    return input()

def input_int() -> int:
    return int(input2())
