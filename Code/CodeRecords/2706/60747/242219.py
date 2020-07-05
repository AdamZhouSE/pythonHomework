import re
s1=str(input())
ri=s1.split("]")
num=[]
d=s1.count("]")-1
for i in range(d):
    num.append(ri[i].count("@")+1)
p = re.compile('.+?"(.+?)"')
s2 = p.findall(s1)
new=[]
a=0
accounts=[]
h=0
for v in range(len(s2)):
    new.append(s2[v])
    a=a+1
    if a==num[h]:
        h=h+1
        accounts.append(new)
        a=0
        new=[]
for k in range(len(accounts)):
    j=k+1
    while j<len(accounts):
        if len(set(accounts[k])&(set(accounts[j])))>=2:
            accounts[k]=list(set(accounts[k]).union(set(accounts[j])))
            del accounts[j]
            j=j-1
        else: j+=1
print(accounts)

s=input()
s=s[1:len(s)-1].split(",")
for i in range(len(s)):
    s[i]=int(s[i])
for i in s:
    if s.count(i)==1 :
        print(i)