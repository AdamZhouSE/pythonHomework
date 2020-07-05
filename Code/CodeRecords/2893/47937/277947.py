s=eval(input())
x=sorted(s)
#print(x)
i=1
if(x[0]!=x[1]):
    print(x[0])
if(x[len(x)-1]!=x[len(x)-2]):
    print(x[len(x)-1])
while i<len(x)-1:
    if(x[i]!=x[i-1] and x[i]!=x[i+1]):
        print(x[i])
    i=i+1
    