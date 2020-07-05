n,k=map(int,input().split())
step=[]
for i in range(n):
    step.append(input().split())
    step[i][0]=int(step[i][0])
painted=[0]
pointer=0
for i in range(n):
    for j in range(step[i][0]):
        if step[i][1]=='R':
            if pointer+1<len(painted):
                pointer+=1
                painted[pointer]+=1
            else:
                painted.append(1)
                pointer+=1
        else:
            painted[pointer]+=1
            if pointer-1<0:
                painted.insert(0,0)
            else:
                pointer-=1
res=0
for i in painted:
    if i>=k:
        res+=1
print(res,end="")