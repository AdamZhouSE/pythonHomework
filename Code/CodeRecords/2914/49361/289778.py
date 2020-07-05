num = int(input())
for i in range(num):
    length = int(input())
    a = input()
    b = input()
    a = [int(x) for x in a.split(" ")]
    b = [int(x) for x in b.split(" ")]
    diff = 0
    exist = True
    for j in range(length):
        if a[j] - b[j] != 0:
            if diff != 0:
                if a[j] - b[j] != diff:
                    exist = False
                    break
            else:
                diff = a[j] - b[j]
    if exist:
        print("YES")
    else:
        print("NO")
