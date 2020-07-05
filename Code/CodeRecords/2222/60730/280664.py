m, n = map(str, input().split("="))
a = list(m)
b = list(n)
flag = True
flag_num = True
temp = 0
xi_Left, xi_Right = 0, 0
num_Left, num_Right = 0, 0
flag = False
for i in range(len(a)):
    if a[i] == "-":
        flag = False
        num_Left += temp
        temp = 0
    elif a[i] == "+":
        flag = True
        num_Left += temp
        temp = 0
    elif str(a[i]).isdigit():
        if i == 0:
            flag = True
            temp = int(a[i])
        else:
            if flag:
                temp = 10 * temp + int(a[i])
            else:
                temp = 10 * temp - int(a[i])
    elif a[i] == "x":
        if i == 0:
            xi_Left += 1
        elif a[i - 1] == "+":
            xi_Left += 1
        elif a[i - 1] == "-":
            xi_Left -= 1
        else:
            xi_Left += temp
        temp = 0

num_Left += temp
flag, temp = True, 0

for i in range(len(b)):
    if b[i] == "-":
        flag = False
        num_Right += temp
        temp = 0
    elif b[i] == "+":
        flag = True
        num_Right += temp
        temp = 0
    elif str(b[i]).isdigit():
        if i == 0:
            flag = True
            temp = int(b[i])
        else:
            if flag:
                temp = 10 * temp + int(b[i])
            else:
                temp = 10 * temp - int(b[i])
    elif b[i] == "x":
        if i == 0:
            xi_Right += 1
        elif b[i - 1] == "+":
            xi_Right += 1
        elif b[i - 1] == "-":
            xi_Right -= 1
        else:
            xi_Right += temp
        temp = 0

num_Right += temp

x = xi_Left - xi_Right
y = num_Right - num_Left
if x == 0 and y == 0:
    print("Infinite solutions")
elif x == 0 and y != 0:
    print("No solution")
elif x != 0:
    ans = int(y / x)
    print("x=" + str(ans))
