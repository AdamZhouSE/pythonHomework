line1=input().split()
N=int(line1[0])
P=int(line1[1])
nums=input().split()

nums=[int(x) for x in nums]
times=int(input())

for i in range(times):
    line1=input().split()
    line1=[int(x) for x in line1]
    if line1[0]==1:
        for i in range(line1[1]-1,line1[2]):
            nums[i]*=line1[3]
    elif line1[0]==2:
        for i in range(line1[1]-1,line1[2]):
            nums[i]+=line1[3]
    else:
        sum=0
        for i in range(line1[1] - 1, line1[2]):
            sum+= nums[i]
        print(sum%P)