import util
import dataclasses


# @dataclasses.dataclass
class employee:
    #emp_no: int
    #emp_name: str
    def __init__(self, emp_no: int, emp_name: str):
        self.emp_no: int = emp_no
        self.emp_name: str = emp_name

    def show_detail(self):
        print(self.emp_name)
        print(self.emp_no)


if __name__ == '__main__':
    print("社員番号を入力してください -> ", end="")
    no: int = int(util.input_int())
    print("社員名を入力してください -> ", end="")
    name: str = input()
    emp = employee(emp_no=no, emp_name=name)
    emp.show_detail()
    x = employee(emp_no=10, emp_name="aaa")
    x.show_detail()
