
import dataclasses
import pdb


@dataclasses.dataclass
class Test:
    value1: int
    value2: str


class Test2:
    value1: int
    value2: str
    value3: int = 100

    def __init__(self, t: int, y: str) -> None:
        self.value1 = t
        self.value2 = y

    def __del__(self) -> None:
        print(f"deleted : {self.value2}")


if __name__ == '__main__':
    """test1: Test = Test(1, "aaa")
    print(f"test1 : {test1.__dict__}")
    test2: Test = Test(2, "bbb")
    print(f"test1 : {test1.__dict__}")"""

    test3: Test2 = Test2(3, "ccc")
    #test3: Test2 = Test2()
    print(f"test3 : {test3.__dict__}")
    print(f"test3 : {test3.value1}")

    test4: Test2 = Test2(4, "ddd")
    #test4: Test2 = Test2()
    Test2.value3 = 5
    print(f"test4 : {test3.__dict__}")
    print(f"test3 : {test3.value3}")
    del test4
    print(f"test3 : {test3.__dict__}")
