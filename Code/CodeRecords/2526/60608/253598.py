import re
def func1():
    tree = []
    tree += list(map(int, re.findall(r'-?\d+', input())))
    tree += list(map(int, re.findall(r'-?\d+', input())))
    print(sorted(tree))


func1()
