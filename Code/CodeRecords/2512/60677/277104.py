def print1(nums,i):
    print("经过第"+str(i)+"次操作后，数列为",end="(")
    nums=[str(x) for x in nums]
    print(",".join(nums),end=")")
    print("。")
    nums=[int(x) for x in nums]

line1=input().split()
N=int(line1[0])
P=int(line1[1])
nums=input().split()
print("初始时数列为",end="(")
print(",".join(nums))
print(")。")
nums=[int(x) for x in nums]
times=int(input())

for i in range(times):
    line1=input().split()
    line1=[int(x) for x in line1]
    if line1[0]==1:
        for i in range(line1[1]-1,line1[2]):
            nums[i]*=line1[3]
        print1(nums,i+1)
    elif line1[0]==2:
        for i in range(line1[1]-1,line1[2]):
            nums[i]+=line1[3]
        print1(nums,i+1)
    else:
        print("对第" + str(i) + "次操作，和为")
        sum=0
        for i in range(line1[1] - 1, line1[2]):
            print(nums[i],end="")
            if(i!=line1[2]-1):
                print("+",end="")
            else:
                print("=",end="")
            sum+= nums[i]
        print(sum,end=",")
        print("模",end="")
        print(P,end="")
        print("的结果是",end="")
        print(sum%P,end=".")
        print()