from typing import Generator


def get_objects() -> Generator:
    yield "a"
    yield "b"


generator = get_objects()
for i in generator:
    print(i)
