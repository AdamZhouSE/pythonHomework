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
                A.append(int(y) // d)
            else:
                flag = 0
                break
if flag:
    A.sort()
    middle = A[(len(A)-1)//2]
    s = 0
    for x in A:
        s += abs(x - middle)
    print(s)
else:
    print(-1)
