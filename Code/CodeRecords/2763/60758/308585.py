out=[]
def deep(m,n,current,num,temp):
    if num==n:
        out.append(temp.copy())
        return
    for i in range(current*2,m+1):
        if i==0:
            continue
        temp.append(i)
        deep(m,n,i,num+1,temp.copy())
        temp=temp[0:len(temp)-1]

for _ in range(int(input())):
    m,n=map(int,input().split())
    out=[]
    deep(m,n,0,0,[])
    print(len(out))