def getkeyvalue(c):
    x=t.count(c)
    return x
t=list(input())
w=sorted(t,key=getkeyvalue,reverse=True)

for i in w:
    print(i,end="")
print()
