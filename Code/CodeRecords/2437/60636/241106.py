location=[]
for i in range(-1000000,1000001):
    location.append(0)
now=1000000
num=input().split(" ")
number=int(num[0])
K=int(num[1])
for i in range(number):
    x=input().split(" ")
    if(x[1]=="L"):
        end=now-int(x[0])
        for a in range(end,now):
            location[a]=location[a]+1
        now=end
    elif(x[1]=="R"):
        end=now+int(x[0])
        for a in range(now,end):
            location[a]=location[a]+1
        now=end
count=0
for x in location:
    if(x>=K):
        count=count+1
print(count,end="")