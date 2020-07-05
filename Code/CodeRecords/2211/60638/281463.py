nums=list(map(int,input().split(" ")))
n=nums[0]
k=nums[1]
names=[]
for x in range(0,n):
    inpu=input().split(" ")
    i=int(inpu[1])
    if i!=0:
        names.append(inpu[0]+names[i-1])
    else:
        names.append(inpu[0])

for x in range(0,k):
    count=0
    name=input()
    for i in range(0,len(names)):
        if names[i].startswith(name):
            count=count+1
    print(count)