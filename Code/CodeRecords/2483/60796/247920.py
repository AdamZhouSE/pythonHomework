
n=int(input())
ls=[]
while n>0:
    l=[]
    l.append(input())
    l.append(input())
    ls.append(l)
    n=n-1


result=[]
for i in range(len(ls)):
    str=ls[i][0]
    patt=ls[i][1]
    min=100000
    f='$'
    for j in range(0,len(patt)):
        if str.__contains__(patt[j]):
            if str.index(patt[j])<min:
                min=str.index(patt[j])
                f=patt[j]
    result.append(f)
for i in range(0,len(result)):
    print(result[i])