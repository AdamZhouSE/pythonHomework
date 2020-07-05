a=eval(input())
k=eval(input())
minmum=len(a)+1
for i in range(len(a)):
    if(a[i]<=0):
        continue
    else:
        total=0
        j=i
        while total<k and j<len(a):
            total+=a[j]
            j+=1
        j-=1
        if(total>=k):
            minmum=min(minmum,j+1-i)
if minmum<len(a)+1:
    print(minmum)
else:
    print(-1)