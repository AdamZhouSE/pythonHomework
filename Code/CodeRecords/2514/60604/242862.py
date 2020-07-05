s=input()
t=input()
def f(a,b):
    for i in range(len(a)):
        if a[i]==b:
            return i
    return -1

j=True
x=0
for i in range(len(s)):
    x=f(t[x:len(t)],s[i])
    if x==-1:
        j=False
        break

print(j)
    