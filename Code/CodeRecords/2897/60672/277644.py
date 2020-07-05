ar=input()
maxx=0
mid=0
indicate=0
for i in range(len(ar)-1):
    for j in range(i+1,len(ar)):
        for k in range(len(ar[i])):
            if ar[i][k]in set(ar[j]):
                indicate=1
                break
        if indicate==0:
            mid=len(ar[i])*len(ar[j])
        if mid>maxx:
            maxx=mid
        indicate=0
print(maxx)