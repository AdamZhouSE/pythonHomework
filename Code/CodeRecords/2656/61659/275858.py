import math

T = int(input())


def turnToBinary(x):
    result = ""
    while x != 0:
        remain = x % 2
        x = int(math.floor(x / 2))
        result = str(remain) + result
    return result


for k in range(0, T):
    temp = list(input().split(" "))
    A = int(temp[0])
    B = int(temp[1])

    a = turnToBinary(A)
    b = turnToBinary(B)
    length = min(len(a), len(b))

    if a!=b:
        x=True
        for j in range(1, length + 1):
            if a[len(a) - j] != b[len(b) - j]:
                print(j)
                x=False
                break
        if x:
            temp=""
            if len(a)<=len(b):
                temp=b
            else:
                temp=a
            temp=temp[0:len(temp)-length]
            temp=temp[::-1]
            a=temp.index("1")
            print(length+a+1)
    else:
        print(-1)
