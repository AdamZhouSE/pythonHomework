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
    count = 0
    for j in range(length):
        if a[j] - b[j] != 0:
            if diff == 0:
                diff = a[j] - b[j]
                count += 1
                continue
            if a[j] - b[j] != diff:
                exist = False
                break
            elif flag == 2:
                exist = False
                break
            else:
                count += 1
        else:
            if diff != 0:
                flag = 2
                continue
    if exist and (count == 0 or ( count > 1 and diff < 0) ):
        print("YES")
    else:
        print("NO")
