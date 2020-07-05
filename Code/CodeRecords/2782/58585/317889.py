def f(a,b):
    if a>b:
        return a-b
    else:
        return b-a
    
n=int(input())
count=0
a=int(input())
count+=a
for i in range(n):
    b=input()
    count+=f(a,b)
    a=b
print(count)