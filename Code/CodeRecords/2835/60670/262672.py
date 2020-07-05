n=int(input())
nums=list(map(int,input().split()))
num_of_5=0
num_of_0=0
for i in nums:
    if i==5:
        num_of_5+=1
    else:
        num_of_0+=1
if num_of_0==0:
    print(0)
else:
    #num_of_0-=1
    num_of_5=num_of_5-(num_of_5%9)
    for i in range(0,num_of_5):
        print("5",end="")
    for i in range(0,num_of_0):
        print("0",end="")
    print()