a=eval(input())
b=[]
for i in a:
    b.extend(map(int,i))
b.sort()
print(b)