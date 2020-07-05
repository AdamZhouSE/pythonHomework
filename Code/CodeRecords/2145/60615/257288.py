
time=int(input())
result=[]
while time>0:
    num=input()
    rec=list(map(int,input().split()))
    height=list(set(rec))
    height.sort(reverse=True)
    space=[]
    for i in height:     #i used
        width=0
        for j in range(0,len(rec)):
            if i<=rec[j]:
                width=width+1
            else:
                if width>0:
                    space.append(width*i)
                    width=0
            if j==len(rec)-1:
                if width>0:
                    space.append(width*i)

    result.append(max(space))
    time=time-1

for res in result:
    print(res)

