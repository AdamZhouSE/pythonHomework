cnt = int(input())
li = []
for i in range(cnt):
    li.append(str(input()))

res = []
for currentStr in li:
    currentLi = list(currentStr)
    last = "-1"
    for now in currentLi:
        if (now != last):
            print(now, end="")
            last = now
    print()