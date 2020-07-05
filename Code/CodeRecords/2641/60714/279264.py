from itertools import permutations

a = input()
b = input()
flag = False
temp = list(permutations(a))
for item in temp:
    if "".join(item) in b:
        flag = True
        print(True)
        break
if not flag:
    print(False)
