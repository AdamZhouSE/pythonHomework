l=input().split()
arr1=input().split()
arr2=input().split()
ans=[]
for num in arr1:
    if num in arr2:
        ans.append(num)
print(" ".join(for i in ans))