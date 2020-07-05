def Ascend(nums:list)->list:
    n=len(nums)
    for i in range(0,n):
        for p in range(i+1,n):
            if nums[i]>nums[p]:
                t=nums[i]
                nums[i]=nums[p]
                nums[p]=t
    return nums
def merge(A1,A2,A3):
    newArray=[]
    n1=len(A1)
    n2=len(A2)
    n3=len(A3)
    n=n1+n2+n3
    A1=Ascend(A1)
    A2=Ascend(A2)
    A3=Ascend(A3)
    for i in range(0,n1):
        newArray.append(A1[i])
    for i in range(0,n2):
        newArray.append(A2[i])
    for i in range(0,n3):
        newArray.append(A3[i])
    newArray=Ascend(newArray)
    return newArray
A1=[1,4,5]
A2=[1,3,4]
A3=[2,6]
print(merge(A1,A2,A3))
