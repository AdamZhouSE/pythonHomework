import re
lst = re.findall(r'\d+',input())
lst = list(map(int,lst))

#最多只能有两个众数
m,n = 0,0
cm,cn = 0,0

for a in lst:
    if a == m:
        cm+=1
    elif a == n:
        cn+=1
    elif cm == 0:
        m = a
        cm = 1
    elif cn == 0:
        n = 1
        cn = 1
    else:#两个计数器都要减一
        cm-=1
        cn-=1
#重新遍历
cm, cn = 0,0
for a in lst:
    if a == m:
        cm+=1
    elif a == n:
        cn+=1
res = []
if cm>len(lst)/3:
    res.add(m)
if cn>len(lst)/3:
    res.add(n)
print(res)