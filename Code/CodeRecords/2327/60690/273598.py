s=input()
n=len(s)
value=0
m=len(s)
list=[]
for i in range(n):
    if s[i]=="I":
        list.append(value)
        value += 1
    else:
        list.append(m)
        m-=1
list.append(value)
print(list)
