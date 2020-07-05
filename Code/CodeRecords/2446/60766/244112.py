def getSequence(res, que):
    c=''
    for i in range(len(res)):
        if que in res[i]:
            c=c+str(i+1)+' '
    return c

n=int(input())
res=[]
for i in range(n):
    line=input().split()
    res.append(line[1:])
m=int(input())
for i in range(m):
    que=input()
    count=getSequence(res, que)
    if len(count)==0 or count=='':
        print(' ')
    else:
        print(count)