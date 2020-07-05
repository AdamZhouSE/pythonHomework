temp=input().split(" ")
n=int(temp[0])
m=int(temp[1])

nums=list(map(int,input().split(" ")))

for i in range(m):
    temp=input().split(" ")
    nums[int(temp[0])-1]=int(temp[1])
    Curnums=nums.copy()
    N=2**n
    which=0
    while(len(Curnums)!=1):
        j=0
        if(which%2==0):
            while(j<N//2):
                Curnums[j]=Curnums[j*2]|Curnums[j*2+1]
                j+=1
        else:
            while (j <N//2):
                Curnums[j] = Curnums[j*2]^Curnums[j*2+1]
                j += 1
        Curnums=Curnums[0:j]
        N=N//2
        which+=1
    print(Curnums[0])