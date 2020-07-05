temp=input().split(" ")
n=int(temp[0])
m=int(temp[1])

tmp=input()
nums=list(map(int,tmp.split(" ")))

for i in range(m):
    temp=input().split(" ")
    if(temp[0]=='Q'):
        part=nums[int(temp[1])-1:int(temp[2])]
        part.sort()
        print(part[int(temp[3])-1])
    else:
        nums[int(temp[1])-1]=int(temp[2])