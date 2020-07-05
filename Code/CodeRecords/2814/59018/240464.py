n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
a.sort()

print(a)
wait=0
k=0
count=0
for i in range(n):
    if count<n:
        if wait<=a[i]:
            k=k+1
            wait=wait+a[i]
        else:
            a.append(a[i])
            a.pop(i)
            i=i-1   
        count=count+1
    else:
        break
print(k)