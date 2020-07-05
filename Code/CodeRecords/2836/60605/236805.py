n = int(input())
tmp = input().split(" ")
li = []
for i in tmp:
    li.append(int(i))
isP = True
newLi = sorted(li)
if newLi == li:
    print("0")
else:
    cnt = 0
    while True:
        cnt += 1
        li.insert(0, li.pop())
        if li == newLi:
            print(cnt)
            isP = False
            break
        if cnt == len(li): break
    if isP: print("-1")