d=input()
a=[x for x in d]
b=eval(input())
if(b>1):
    a.sort()
    st=""
    for i in a:
        st+=i
    print(st)
else:
    a.sort()
    i=d.find(a[0])
    str=d[i:]+d[0:i]
    print(str)