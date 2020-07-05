num = int(input())
for i in range(num):
    length = int(input())
    a = input()
    b = input()
    a = [int(x) for x in a.split(" ")]
    b = [int(x) for x in b.split(" ")]
    diff = 0
    exist = True
    flag = 0
    for j in range(length):
        if a[j] - b[j] != 0:
            diff = a[j] - b[j]
            if a[j] - b[j] != diff:
                exist = False
                break
            elif flag == 2:
                exist = False
                break
        else:
            if diff != 0:
                flag = 2
                break
    if exist:
        print("YES")
    else:
        print("NO")
