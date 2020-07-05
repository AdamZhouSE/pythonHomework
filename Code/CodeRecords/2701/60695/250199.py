def check(a):
    if 0 in a and 1 in a and 2 in a:
        return True
    elif 0 in a and 3 in a and 6 in a:
        return True
    elif 0 in a and 4 in a and 8 in a:
        return True
    elif 3 in a and 4 in a and 5 in a:
        return True
    elif 6 in a and 7 in a and 8 in a:
        return True
    elif 1 in a and 4 in a and 7 in a:
        return True
    elif 2 in a and 5 in a and 8 in a:
        return True
    elif 2 in a and 4 in a and 6 in a:
        return True
    else:
        return False


steps = input()
set = []
for i in steps:
    if i.isdigit():
        set.append(i)
n = int(len(set) / 2)
A = []
B = []

flag = True
i = 0
while i < n:
    if i % 2 == 0:
        A.append(int(set[i*2])*3+int(set[i*2+1]))
        if check(A) is True:
            print("A")
            flag = False
            break
    else:
        B.append(int(set[i*2])*3+int(set[i*2+1]))
        if check(B) is True:
            print("B")
            flag = False
            break
    i += 1
if flag:
    if i == 9:
        print("Draw")
    else:
        print("Pending")