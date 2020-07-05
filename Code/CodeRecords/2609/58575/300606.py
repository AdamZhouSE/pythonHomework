num=int(input())
result=list()
for i in range(num):
    str1=list(map(int,input().split(" ")))
    nums=input().split(" ")
    res={}
    for j in nums:
        if j not in res:
            res[j]=1
        else:
            res[j]=res[j]+1
    judge=0
    for i in res:
        if res[i]==1:
            judge=judge+1
        if judge==str1[1]:
            result.append(int(i))
            break
    if judge!=str1[1]:
        result.append(-1)
for i in result:
    print(i)