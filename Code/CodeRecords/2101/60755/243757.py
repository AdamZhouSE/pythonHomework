i = int(input())
flag = 0
for k in range(1000):
    if i == "1":
        flag = 1
    else:
        sum = 0
        for x in str(i):
            sum = sum + int(x) * int(x)
        i = str(sum)
if flag:
    print("True")
else:
    print("False")