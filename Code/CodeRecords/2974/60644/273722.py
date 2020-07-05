#长度为l的正回文子串个数
def f(arr,l):
    a=[]
    res=0
    for i in range(0,len(arr)-l+1):
        p=True
        for j in range(i,i+l):
            if arr[j]!=arr[2*i+l-j-1]:
                p=False
                break
        if p and l%2==1 and a.count(','.join(arr[i:i+l]))==0:
            res+=1
            a=a+[','.join(arr[i:i+l])]
    return res

#长度为l的非正回文子串个数
def g(arr,l):
    a=[]
    res=0
    for i in range(0,len(arr)-l+1):
        p=True
        for j in range(i,i+l):
            if arr[j]!=arr[2*i+l-j-1]:
                p=False
                break
        if ((not p) or l%2==0) and a.count(','.join(arr[i:i+l]))==0:
            res+=1
            a = a + [','.join(arr[i:i + l])]
    return res

N=int(input())
s=input()
max=0
for i in range(1,10):
    A=list(s[0:i])
    B=list(s[i:])
    s1=0
    s2=0
    for j in range(1,i+1):
        s1=s1+f(A,j)
    for j in range(1,len(B)+1):
        s2=s2+g(B,j)
    if s1*s2>max:
        max=s1*s2
print(max)

