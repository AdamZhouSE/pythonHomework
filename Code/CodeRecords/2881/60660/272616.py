t=int(input())
n=t//2
l=[]
for i in range(n):
    element='*'*((t-(2*i+1))//2)+'D'*(2*i+1)+'*'*((t-(2*i+1))//2)
    l.append(element)
l.append('D'*t)
for i in range(len(l)):
    print(l[i])
for i in range(len(l)-2,-1,-1):
    print(l[i])