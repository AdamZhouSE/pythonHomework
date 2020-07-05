a=eval(input())
num=0
b=[]
for i in range(1,a):
    t=2*a+i-i**2
    if(t%(2*i)==0):
        b.append(t/(2*i))
print(len(set(b)))