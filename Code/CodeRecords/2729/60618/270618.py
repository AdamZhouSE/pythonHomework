a=eval(input())
b=list(set(a))
for i in range(0,len(b)):
    if a.count(b[i])==1:
        print(b[i])