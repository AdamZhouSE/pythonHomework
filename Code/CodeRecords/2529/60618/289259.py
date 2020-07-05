import itertools
a=list(itertools.permutations(list(str(input()))))
s=''
result=0
for x in a:
    if x[0]!="0":        
        for i in range(0,len(x)):
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
    if m1.count("1")==1 and m1[0]=="0" and m1[len(m1)-1]=="1":
        result=1
    elif len(m1)==1 and m=="1":
        result=1
if result==1:
    print("true")
else:
    print("false")
        
'''    
    for i in range(0,10000):
        if int(s)==2**i:
            result=1
            break
if result==1:
       print("true")
else:
       print("false")
'''