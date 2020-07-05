a=eval(input())
last=0
for i in range(0,len(a)):
    for x in range(i+1,len(a)):
        index=0
        for j in range(0,len(a[i])):
            if a[i][j] in a[x]:
                index=1
        if index==0 and len(a[i])+len(a[x])>last:
            last=len(a[i])+len(a[j])
if last==0:print(26)
else:
    print(last)
    