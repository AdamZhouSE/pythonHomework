num = int(input())
all = []
for i in range(num):
    n = input()
    all.append(input().split(" "))
for i in all:
    flag = False
    for k in range(len(i)):
        if i.count(i[k])!=1:
            print(k+1)
            flag = True
            break
    if not flag:
        print(-1)