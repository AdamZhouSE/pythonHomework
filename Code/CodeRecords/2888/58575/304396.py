nums=input().split(" ")
n=int(nums[0])
m=int(nums[1])

num=list(map(int,input().split(" ")))

numberOfPos=0
numberOfNeg=0

for i in num:
    if i==1:
        numberOfPos+=1
    elif i==-1:
        numberOfNeg+=1

for i in range(m):
    temp=input().split(" ")
    l=int(temp[0])
    r=int(temp[1])

    if((r-l+1)%2==1):
        print(0)
    else:
        if numberOfNeg<(r-l+1)//2 or numberOfPos<(r-l+1)//2:
            print(0)
        else:
            print(1)