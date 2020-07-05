str = int(input())

present = str
number = 0
while present > 0:
    lst = []
    while str > 0:
        left = str % 10
        lst.insert(0, left)
        str = int(str / 10)
    number += lst.count(1)
    present -= 1
    str = present

print(number)