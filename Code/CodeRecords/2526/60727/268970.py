import re
def so():
    tree = []
    tree += list(map(int, re.findall(r'-?\d+', input())))
    tree += list(map(int, re.findall(r'-?\d+', input())))
    print(sorted(tree))
so()