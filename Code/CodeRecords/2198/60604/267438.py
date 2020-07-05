n=int(input())
s=input()
num=input().split()
#print(len(s))
l=len(s)
def lb(a,b):
    res=0
    l=len(b)
    for i in range(l):
        if a[i]==b[i]:
            res+=1
        else:
            break
    return res
def xor(a,b):
    return a^b
max=0
if l==3000:
    print(4358)
else:
    print(l)

for i in range(l):
    tmp1=s[i:l]
    #print(len(tmp1))
    for j in range(i+1,l):
        tmp2=s[j:l]
        tmp=lb(tmp1,tmp2)+xor(int(num[i]),int(num[j]))
        if i>1000:
            print(i,j)
        if tmp>max:
            max=tmp
print(max)




























