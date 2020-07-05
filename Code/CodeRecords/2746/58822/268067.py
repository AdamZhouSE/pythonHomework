def notcommon(a,b):
    n=0
    for i in a:
        if(i not in b):
            n+=1
    return n
a=input()
b=input()
c=input()
c=eval(c)
num=notcommon(a,b)
z=b
candi=[]
if(b not in c):
    print(0)
    exit()
for i in range(num):
    candi.append([])
for i in range(1,num+1):
    for ele in c:
        if(notcommon(a,ele)==i):
            candi[i-1].append(ele)
for i in range(0,num):
    if(len(candi[i])==0):
        print(0)
        exit()
print(2*num-1)