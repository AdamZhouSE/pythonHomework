lineNO = int(input())
lines = list(map(int, input().split()))

def judgeTri():
    flag = False
    for i in range(lines.__len__() - 2):
        if (lines[i] + lines[i + 1] > lines[i + 2]) and (lines[i] + lines[i + 2] > lines[i + 1]) and (lines[i + 1] + lines[i + 2] > lines[i]):
            flag = True
    return flag

if judgeTri():
    print("YES")
else:
    print("NO")