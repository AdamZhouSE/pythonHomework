s=input()
orders=input()
order=[]
for i in orders:
    if i.isalpha() or i.isdigit():
        order.append(i)
if order[0]=='D':
    if s.index(order[1])!=-1:
        s=s[:s.index(order[1])]+s[s.index(order[1])+1:]
    else:
        print("no exist")
elif order[0]=='I':
    if s.rindex(order[1])!=-1:
        s=s[0:s.rindex(order[1])]+order[2]+s[s.rindex(order[1]):]
    else:
        print("no exist")
elif order[0]=='R':
    if order[1] in s:
        s=s.replace(order[1],order[2])
    else:
        print("no exist")
print(s)

