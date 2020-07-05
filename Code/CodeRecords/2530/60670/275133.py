def strcmp(a,b):
    if s.index(a)<s.index(b):
        return -1
    if s.index(a)>s.index(b):
        return 1
    return 0

s=input()
t=input()
t_in_s=[]
t_not_in_s=""
for c in t:
    if c in s:
        t_in_s.append(c)
    else:
        t_not_in_s+=c
t_in_s=sorted(t_in_s,key=strcmp)
ans=""
for c in t_in_s:
    ans+=c
ans+=t_not_in_s
print(ans)