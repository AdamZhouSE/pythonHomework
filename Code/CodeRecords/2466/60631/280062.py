def judge(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        return True
    else:
        return False

t=int(input())
for ti in range(t):
    n = int(input())
    li = input().split(' ')
    out=0
    data=[]
    for i in range(len(li)):
        for j in range(i+1,len(li)):
            for k in range(j+1,len(li)):
                if judge(int(li[i]),int(li[j]),int(li[k])):
                    out=out+1
                #print(int(li[i]),int(li[j]),int(li[k]))
                
    print(out)