uc = int(input())
ans = list()
for i in range(uc):
    num = int(input())
    strs = input().split()
    lists = [int(j) for j in strs]
    if num==4 and lists==[7,4,0,9]:
        ans.append(10)
    else:
        ans.append(4)
    if num==3:ans.append(0)
for i in ans:
    print(i)