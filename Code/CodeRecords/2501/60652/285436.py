n=int(input())
arr1=list(input().split())
arr2=list(input().split())
diff=0
for i in range(len(arr1)-1):
    for j in range(i+1,len(arr1)):
        a,b=arr2.index(arr1[i]),arr2.index(arr1[j])
        if a>b:
            diff+=1
print(diff)            