# Memo from : https://medium.com/bitgrit-data-science-publication/python-f-strings-tricks-you-should-know-7ce094a25d43
# Formatting numbers

number = 330

print(f"number: {number:.2f}")  # decimal
print(f"hex: {number:#0x}")  # hex
print(f"binary: {number:b}")  # binary
print(f"octal: {number:o}")  # octal
print(f"scientific: {number:e}")  # scientific
print(f"Number: {number:09}")  # number of characters

import datetime

today = datetime.datetime.utcnow()
print(f"datetime : {today}\n")

print(f"date time: {today:%m/%d/%Y %H:%M:%S}")
print(f"date: {today:%m/%d/%Y}")
print(f"time: {today:%H:%M:%S.%f}")
print(f"time: {today:%H:%M:%S %p}")
print(f"time: {today:%H:%M}")

from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int

    def __str__(self) -> str:
        return f"{self.name} is {self.age} years old"


toto = Person("toto tutu", 69)
print(f"{toto}")  # str
print(f"{toto!r}")  # repr

# alignment

number = 4
print(f"number is {number:4}")  # width of 10

# numbers
for number in range(1, 5):
    print(f"the number is {number:{number}}")

left = "left text"
center = "center text!"
right = "right text"

print(f"{left:>20}")  # left align
print(f"{center:^20}")  # center align
print(f"{right:<20}")  # right align

print(f"{left : <20}{center : ^20}{right : >20}")
