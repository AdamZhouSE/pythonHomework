a=input()
b=input()
def isForm(x,y,a):
    
    x1=27
    y1=27
    for i in range(len(a)):
        if x==a[i]:
            x1=i
        if y==a[i]:
            y1=i
    return x1<y1
c=list(b)
for i in range(len(b)):
    for j in range(len(b)-1,i,-1):
        if isForm(b[j],b[j-1],a):
            tmp=c[j]
            c[j]=c[j-1]
            c[j-1]=tmp
print("".join(c))