def rotate(str):
    a = len(str)
    i = 0
    while i < a:
        if str[i] != str[a - 1 - i]:
            return False
        i += 1
    if i == a:
        return True

def change(str):
    temp = str[::-1]
    return temp

def lalala(str):
    if len(str) == 1:
        print(1)
    else:
        result = len(str)
        size = len(str)
        i = 2
        while i <= size:
            x = 0
            while x + i <= size:
                if rotate(str[x:x + i]):
                    result += 1
                x += 1
            i += 1
        print(result)


str = input()
i = int(input())
for j in range(i):
    l = input().split()
    if l[0] == "3":
        lalala(str)
    elif l[0] == "1":
        str = str + l[1]
    else:
        str = change(l[1]) + str