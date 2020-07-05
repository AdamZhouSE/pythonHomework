str1 = input().split()
n = int(str1[0])
m = int(str1[1])
d = int(str1[2])
r = -1
flag = 1
A = []
for x in range(n):
    if flag == 0:
        break
    str2 = input().split()
    for y in str2:
        if r == -1:
            r = int(y) % d
            A.append(int(y) // d)
        else:
            if int(y) % d == r:
                if int(y) // d not in A:
                    A.append(int(y) // d)
            else:
                flag = 0
                break
if flag:
    print(len(A))
else:
    print(-1)
