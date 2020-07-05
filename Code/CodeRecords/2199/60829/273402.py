def find(s):
    res=""
    count=0
    for i in range(0,len(s)-1):
        for j in range(i+1,len(s)):
            if ju(s,cc(s,i,j)) and j+1-i>count:
                res=cc(s,i,j)
                coount=j+1-i
    if res=="":
        for i in range(len(s)):
            if ju(s,s[i]):
                res=s[i]
    return res
def cc(x,i,j):
    xx=""
    for k in range(i,j+1):
        xx=xx+x[k]
    return xx
def ju(a,b):
    count=0
    for i in range(0,len(a)-len(b)+1):
        if a[i]==b[0]:
            judge=0
            for j in range(0,len(b)):
                if  not a[i+j]==b[j]:
                    judge=1
                    break
            if judge==0:
                count=count+1
    if count>1:
        return True
    else:
        return False
s=str(input())
count=1
while not s=="":
    count=count+1
    s=find(s)
print(count)