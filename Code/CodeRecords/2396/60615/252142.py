n=int(input())
num=list(map(int,input().split()))
start=0
index=[]
while(n>0):
    rel_min=min(num)

    p=num.index(rel_min)
    index.append(start+p+1)
    sub=num[:p+1]
    sub.reverse()

    begin = 0
    for i in sub:

        num[begin] = i
        begin = begin + 1
    start = start + 1
    num = num[1:]
    n = n - 1
for i in index:
    print(i,end=' ')