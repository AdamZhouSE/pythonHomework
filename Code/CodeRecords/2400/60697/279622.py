import sys
N=210
res=[]
for line in sys.stdin:
    res=res+list(map(int,line.split(' ')))
count=-1
cnt=1
sum=[0 for i in range(N)]
def build(p):
    global count,sum
    count+=1
    if(count>=len(res)):
        return 
    v=res[count]
    if(v==-1):
        return
    sum[p]=sum[p]+v
    build(p-1)
    build(p+1)
def input():
    global count,sum
    count+=1
    if (count >= len(res)):
        return
    v=res[count]
    if(v==-1):
        return False
    sum=[0 for i in range(N)]
    pos=N//2
    sum[pos]=v
    build(pos-1)
    build(pos+1)
    return True
while(input()):
    p=0
    while(sum[p]==0):
        p+=1
    print("Case %d:"%cnt)
    cnt+=1
    print(sum[p],end="")
    p+=1
    while(sum[p]>0):
        print(" %d"%sum[p],end="")
        p+=1
    print()
    print()







