def con(n):
    sum = 0
    for i in range(1, len(n) - 1):
        if (n[i - 1] == 1 and n[i + 1] == 1):
            sum += 1
    return sum
num=int(input())
n=input().split(' ')
n=list(map(int,n))
sum=0
li=[]
for i in range(1,len(n)-1):
    if(n[i-1]==1 and n[i+1]==1 and n[i]==0):
        li.append(i)
        sum+=1
if(sum==0):
    print(0)
    exit()
time=0
while(len(li)!=0):
    if(len(li)>1):
        if(li[0]==(li[1])-2):
            del li[0]
            del li[0]
            time+=1
        else:
            time+=1
            del li[0]
    else:
        time+=1
        del li[0]
    
print(time)