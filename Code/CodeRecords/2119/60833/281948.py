x=list(input().split(','))
x=list(map(int,x))
judge=1
if len(x)<=3:
    print(False)
else:
    for i in range(3,len(x)):
        if((x[i]>=x[i-2])&(x[i-3]>=x[i-1])):
            print(True)
            judge=0
            break
        if((i>=4)&(x[i-1]==x[i-3])&(x[i]>=x[i-2]-x[i-4])):
            print(True)
            judge=0
            break
        if((i>=5)&(x[i-2]>=x[i-4])&(x[i-3]>=x[i-1])&(x[i-1]>=x[i-3]-x[i-5])&(x[i]>=x[i-2]-x[i-4])):
            print(True)
            judge=0
            break
    if judge:
        print(False)