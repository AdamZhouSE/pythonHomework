def find(a):
    count=0
    sum=0
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            count=judge(a[i:j+1])
            if count > sum:
                sum = count
    return sum
def judge(x):
    count=1
    cc=x[0]
    for i in range(1,len(x)):
        if x[i]>cc:
            count=count+1
            cc=x[i]
    return count
def dele(x):
    z=""
    for i in range(0,len(x)):
        if not x[i]==" " and not x[i]=="(" and not x[i]==")" and not x[i]=="[" and not x[i]=="]":
            z=z+x[i]
    return z
aa=str(input())
a=[int(x) for x in dele(aa).split(",")]
x=find(a)
print(x)