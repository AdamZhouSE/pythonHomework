n=int(input())
res=[]
number=0
for i in range(n):
    temp=input().split(" ")
    x=int(temp[0])
    y=int(temp[1])
    res.append([x,y])
    number+=1
i=0
times=0
while i<number-1:
    j=i+1
    while j<number:
        one=abs(res[i][0]-res[j][0])+abs(res[i][1]-res[j][1])
        second=(res[i][0]-res[j][0])**2+(res[i][1]-res[j][1])**2
        if second==one**2:
            times+=1
        j+=1
    i+=1
print(times)