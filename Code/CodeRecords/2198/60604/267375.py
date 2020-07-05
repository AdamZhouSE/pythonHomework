n=int(input())
s=input()
num=input().split()
tmp1=[]
for i in range(0,n):
    tmp=[]
    tmp.append(num[i])
    tmp.append(s[i:n])
    tmp1.append(tmp)
print(tmp1)
def lb(a,b):
    a=a[1]
    b=b[1]
    res=0
    l=max(len(a),len(b))
    for i in range(l):
        if a[i]==b[i]:
            res+=1
        else:
            break
    return res
def xor(a,b):
    a=int(a[0])
    b=int(b[0])
    return a^b
max=0
for i in range(1,len(tmp1)):
    for j in range(i+1,len(tmp1)):
        tmp=lb(tmp1[i],tmp1[j])
        tmp+=xor(tmp1[i],tmp1[j])
        if tmp>max:
            max=tmp
print(max)




























