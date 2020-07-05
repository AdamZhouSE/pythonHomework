li=list(eval(input()))
t=int(input())
if li.count(t)==0:
    print('-1')
else:
    print(li.index(t))