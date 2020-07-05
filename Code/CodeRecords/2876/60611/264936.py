num=int(input())
l=list(map(int,input().split()))
lightNumber=0
for i in range(num):
    if l[i]==0 and i!=0 and i!=num-1:
        if l[i-1]==l[i+1]==1:
            lightNumber+=1
            l[i+1]=0
print(lightNumber)