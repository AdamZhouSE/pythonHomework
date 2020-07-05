arr1 = input()
arr2 = input()
alength = len(arr1)
blength = len(arr2)
if alength>blength:
    arr1,arr2=arr2,arr1
nmax = max(alength,blength)
nmin = min(alength,blength)
ans = 0
#arr1 shorter 
for i in range(nmin):
    for j in range(i+1,nmin+1):
        for k in range(nmax):
            if j-i>nmax-k:
                break
            if arr1[i:j]==arr2[k:k+j-i]:
                ans+=1
print(ans)