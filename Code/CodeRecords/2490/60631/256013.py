a=eval(input())
b=eval(input())
out=[]
for i in a:
    if i in b:
        out.append(i)
out = sorted(out)
print(out)