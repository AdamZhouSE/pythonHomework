def shuzu(a):
    counts=[]
    l=0
    while l<len(a):
        i=l+1
        count=0
        while i<len(a):
            if a[l]>a[i]:
                count=count+1
            i=i+1
        l=l+1
        counts.append(count)
    return counts
a=eval(input())
print(shuzu(a))