def dif(s):
    li=list(s)
    li=list(tuple(set(li)))
    return len(li)
def appear(s,sub):
    count=0
    for i in range(len(s)-len(sub)+1):
        if s[i:i+len(sub)]==sub:
            count+=1
    return count
s=input()
maxletter=int(input())
minsize=int(input())
maxsize=int(input())
maxa=0
for i in range(minsize,maxsize+1):
    for j in range(len(s)-i+1):
        tmp=s[j:j+i]
        if dif(tmp)<=maxletter:
            m=appear(s,tmp)
            if m>maxa:
                maxa=m
print(maxa)
        
