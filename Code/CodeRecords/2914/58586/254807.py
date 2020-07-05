nums=int(input())
for i in range(nums):
    length=int(input())
    arr1=list(map(int,input().split(" ")))
    arr2=list(map(int,input().split(" ")))
    left=0
    right=length-1
    for j in range(length):
        if arr1[j]!=arr2[j]:
            left=j
            break
    for j in range(length-1,-1,-1):
        if arr1[j]!=arr2[j]:
            right=j
            break
    def isValid(arr1,arr2):
        dif=arr2[0]-arr1[0]
        if dif<0:
            return False
        for m in range(1,len(arr1)):
            if arr2[m]-arr1[m]!=dif:
                return False
        return True
    res=isValid(arr1[left:right+1],arr2[left:right+1])
    if res:
        print("YES")
    else:
        print("NO")