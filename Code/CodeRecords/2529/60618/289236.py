import itertools
a=list(itertools.permutations(list(str(input()))))
s=''
re=0
result=0
for x in a:
    for i in range(0,len(x)):
        if x[0]=="0":
            break
        else:
            s+=x[i]
    num=int(s)
    m=''
    while num>0:
        if num%2==0:
            m+="0"
        else:
            m+="1"
        num=num//2
    m1=list(m)
    if m1.count("1")==1 and m1[0]=="0":
        result=1
if result==1:
    print("true")
else:
    print("false")
