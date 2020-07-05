n,m=map(int,input().split(" "))
num=[int(i) for i in input().split(" ")]
def func(sign,l,r):
    temp=sorted(num[l-1:r])
    if sign==1:
        temp.reverse()
    for i in range(l-1,r):
        num[i]=temp[i-l+1]
for i in range(0,m):
    sign,l,r=map(int,input().split(" "))
    func(sign,l,r)
q=int(input())
print(num[q-1])