a=eval(input())
def fir(eke):
    return eke[0]
a.sort(key=fir)
i=1
while i<len(a):
    if(a[i][0]<=a[i-1][1] and a[i-1][0]<=a[i][0]):
        a[i-1][1]=max(a[i-1][1],a[i][1])
        a.pop(i)
    else:
        i+=1
print(a)