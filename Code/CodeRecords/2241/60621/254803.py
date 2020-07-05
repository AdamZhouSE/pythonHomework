a=eval(input())
num=0

for i in range(1,a):
    t=2*a+i-i**2
    if(t%(2*i)==0):
        if t/(2*i)>0:
            num+=1
print(num)
