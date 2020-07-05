a=eval(input())
b=eval(input())
s=[]
for i in a:
    if i in b:
        s.append(i)
s.sort()
print(s)