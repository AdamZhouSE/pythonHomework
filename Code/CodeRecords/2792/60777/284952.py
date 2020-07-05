n=int(input())
stair=[int(x) for x in input().split(' ')]
num=1
to=1
out=[]
for i in range(n):
    if(stair[i]==1 ):
        if(i!=0):
            num+=1
            out.append(to)
            to=1        
    else:
        to+=1
out.append(to)       
print(num)
for i in range(num):
    if(i!=(num-1)):
        print(out[i],end=' ')
    else:
        print(out[i])
    