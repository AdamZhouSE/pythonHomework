temp1 = input()
temp2 = input()
if temp1 == "":
    print(temp2)
elif temp2 == "":
    print(temp1)
else:
    a = eval(temp1)
    b = eval(temp2)
    a.extend(b)
    a.sort()
    print(a)