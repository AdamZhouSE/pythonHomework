arr=input()
n=len(arr)
k=0
start=0
amax=0
indexx=0
for i in range(n):
    if int(arr[i])==amax:
        indexx=i
        brr=arr[start:i+1]
        if int(max(brr))==i:
            k=k+1
            amax=i+1
            start=i+1
        else:
            break
print(k)