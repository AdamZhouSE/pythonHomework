tmp=input().split(' ')
n=int(tmp[0])
m=int(tmp[1])
nums=list(map(int,input().split(' ')))
for i in range(m):
    op = list(map(int, input().split(' ')))
    tmp=[]
    for z in range(op[1],op[2]):
        tmp.append(nums[z])
    tmp.sort()
    if(op[0]==1):
        tmp.reverse()
    for z in range(len(tmp)):
        nums[z+op[1]]=tmp[z]

k=int(input())
print(nums[k-1])


