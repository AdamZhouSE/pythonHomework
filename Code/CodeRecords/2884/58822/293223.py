n=input().split(' ')
num=int(n[0])
d=int(n[1])
li=input().split(' ')
li=list(map(int,li))
li.sort()
times=0
for i in range(len(li)):
    for k in range(i+1,len(li)):
        if(li[k]-li[i])<=d:
            times+=1
print(times*2)