def find(n,all):
    new = []
    for i in all:
        if i>=n:
            new.append(i)
    if len(new)==0:
        return 0
    else:
        return min(new)


num = int(input())
flag = True
all = input().split(" ")
for i in range(len(all)):
    all[i]=int(all[i])
for i in range(len(all)):
    temp = find(i+1,all)
    if temp:
        all.remove(temp)
    else:
        print(i)
        flag = False
        break
if flag:
    print(num)