def find(a):
    count=0
    sum=0
    for i in range(0,len(a)-1):
        for j in range(i+1,len(a)):
            if judge(a[i:j]):
                count=j-i
                if count>sum:
                    sum=count
    return sum
def judge(x):
    for i in range(1,len(x)):
        if x[i]<=x[i-1]:
            return False
    return True
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