a=eval(input())
for i in range(1,len(a)):
    count=0
    for m in a:
        if(m<=i):
            count=count+1
    if(count!=i):
        print(i)
    break
