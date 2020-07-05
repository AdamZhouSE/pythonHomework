n=int(input())
nn=input().split()
a=[]
def op(a):
    b=[]
    tmp=[]
    for i in range(1,len(a)):
        for j in range(len(a)-i+1):
            if not a[j:j+i] in tmp:
                tmp.append(a[j:j+i])
    return len(tmp)+1
for i in range(len(nn)):
    a.append(nn[i])
    print(op(a))