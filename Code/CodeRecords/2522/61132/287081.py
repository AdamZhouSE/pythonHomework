def cmp(l):
    def f(a):
        return l.index(a)
    return f

l1=eval(input())
l2=eval(input())
l=[]
for i in range(len(l1)):
    if l1[i] not in l2:
        l.append(l1[i])
        l1[i]='x'
l1 = list(filter(lambda x:x!='x',l1))
f=cmp(l2)
print(sorted(l1,key=f)+sorted(l))