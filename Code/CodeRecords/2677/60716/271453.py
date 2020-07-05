ucnum = int(input())
ans = list()
for i in range(ucnum):
    num = int(input())
    strs = input().split()
    lists = [int(k) for k in strs]
    index=0
    for j in range(len(lists)):
        for t in range(j+1,len(lists)):
            temp = lists[j] ^ lists[t]
            if temp==0: index+=1
    ans.append(index)
for i in ans:
    print(i)