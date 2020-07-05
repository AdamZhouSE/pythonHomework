x=input().split()
n=int(x[0])
m=int(x[1])
a=input().split()
def sheng(a,begin,end):
    tmp=a[begin:end]
    tmp.sort()
    for i in range(begin,end):
        a[i]=tmp[i-begin]
def jiang(a,begin,end):
    tmp=a[begin:end]
    tmp.sort()
    tmp.reverse()
    for i in range(begin,end):
        a[i]=tmp[i-begin]
for i in range(len(a)):
    a[i]=int(a[i])
for i in range(m):
    x=input().split()
    if x[0]=='0':
        sheng(a,int(x[1])-1,int(x[2]))
    else:
        jiang(a,int(x[1])-1,int(x[2]))
b=int(input())
print(a[b-1])