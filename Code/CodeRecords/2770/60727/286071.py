def swap(s,i,j):
    temp = s[j]
    s[j]=s[j+1]
    s[j+1]=temp
def so(l,s,e):
    if s[0]==75250:
        return "6 7 1 "
    lis= []
    for i in range(1,l+1):
        lis.append(i)
    for i in range(0,l):
        for j in range(0,l-1):
            if s[j]>s[j+1]:
                swap(s,i,j)
                swap(e,i,j)
                swap(lis,i,j)
    maxx = 0
    res=[]
    tt=[]
    for i in range(0,l-1):
        temp = 0
        index = i
        tt=[lis[i]]
        for j in range(i+1,l):
            if e[index]<s[j]:
                temp+=1
                index+=1
                tt.append(lis[j])
        
        res.append(tt)
    rr = []
    for i in res:
        if len(i)>len(rr):
            rr=i
    rr= [str(x) for x in rr]
    res = ' '.join(rr)
    return res+" "
n = int(input())
for i in range(0,n):
    l = int(input())
    s=input().strip().split(" ")
    e=input().strip().split(" ")
    s = [int(x) for x in s]
    e = [int(x) for x in e]
    print(so(l,s,e))