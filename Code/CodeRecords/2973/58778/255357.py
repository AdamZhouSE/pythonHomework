s=input()
n=int(input())
def perm(s=''):
    if len(s) <= 1:
        return [s]
    sl = []
    for i in range(len(s)):
        for j in perm(s[0:i] + s[i + 1:]):#去掉第i个字符
            sl.append(s[i] + j)
    return sl
sum=0
for i in range(n):
    st=input()
    c=0
    temp=perm(st)
    temp=list(set(temp))
    for j in temp:
        if(j in s):
            c=c+1
    sum=sum+c
print(sum)