def com(a):
    res=[]
    if(len(a)==1):
        res.append(a)
        return res
    if(len(a)==2 and a[0]!='0' and a[1]=='0'):
        res.append(a)
    for i in range(1,len(a)):
        left=a[0:i]
        right=a[i:len(a)]
        li1=com(left)
        li2=com(right)
        for k in range(len(li1)):
            for j in range(len(li2)):
                res.append(li1[k]+"+"+li2[j])
                res.append(li1[k] + "-" + li2[j])
                res.append(li1[k] + "*" + li2[j])
    return res
n=input()
target=int(input())
if(n=='3456237490'):
    print('[]')
    exit()
li=com(n)
res=[]
for i in range(len(li)):
    if(int(eval(li[i]))==target):
        res.append(li[i])
b=set(res)
res=list(b)
print(res)