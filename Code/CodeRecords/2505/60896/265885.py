a=eval(input())
d=True
for i in range(1,len(a)+1):
    count=0
    for m in a:
        if(m<=i):
            count=count+1
    if(count>i):
        print(i)
        break
    if(count==i and d==False):
        print(i)
        break
    if(count!=i):
        d=False
    if(not d and i==len(a)):
        print(i)