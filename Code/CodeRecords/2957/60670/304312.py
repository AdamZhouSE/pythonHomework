def strange(ss):
    nn=len(ss)
    cnt=1
    for i in range(1,nn):
        if ss[i]!=ss[i-1]:
            cnt+=1
        if cnt>2:
            return False
    return True

s=input()
n=len(s)
cnt=0
for i in range(0,n):
    for j in range(i+1,n+1):
        tmp=s[i:j]
        if strange(tmp):
            cnt+=1
print(cnt)