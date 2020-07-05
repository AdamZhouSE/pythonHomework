a=input().lstrip('[').rstrip(']').split(',')

for i in range(len(a)):
    a[i]=int(a[i])
#print(a)
def spl(a):
    l=len(a)
    res=[]
    for i in range(l-1):
        tmp1=a[0:i+1]
        tmp2=a[i+1:l]
        tmp1.sort()
        tmp2.sort()
        if tmp1[-1]<=tmp2[0]:
            res.append(i)
    return res
#res中每个值代表可以在a[i]后分开
print(len(spl(a))+1)
