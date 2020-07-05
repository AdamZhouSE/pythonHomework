def findmax(a):
    j=0
    num=a[0]
    for i in range(1,len(a)):
        if a[i]>num:
            num=a[i]
            j=i
    return j
def pancakeSort(a):
    i=len(a)
    length=len(a)
    ans=[]
    while i>0:
        b=[]
        c=[]
        x=findmax(a[:i])
        if x==0:
            ans.append(i)
            for j in range(0,i):
                c.append(a[i-j-1])
            if i!=length:
                for j in range(i,length):
                    c.append(a[j])
            a=c
            i=i-1
            continue
        if x!=i-1:
            for j in range(0,x+1):
                b.append(a[x-j])
            for j in range(x+1,i):
                b.append(a[j])
            ans.append(x+1)
            for j in range(0,len(b)):
                c.append(b[len(b)-1-j])
            for j in range(len(b),length):
                c.append(a[j])
            a=c
            ans.append(i)
            i=i-1
        else:
            i=i-1
    ans.pop()
    return ans
a=eval(input())
print(pancakeSort(a))