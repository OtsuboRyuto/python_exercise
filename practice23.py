import dataclasses
import util as ut


@dataclasses.dataclass
class employee:
    emp_no: int
    emp_name: str


if __name__ == '__main__':
    print("社員番号を入力してください -> ", end="")
    no = int(ut.input_int())
    print("社員名を入力してください -> ", end="")
    name = input()
    emp = employee(emp_no=no, emp_name=name)
    print(f"{emp.emp_name}\n{emp.emp_no}")
    