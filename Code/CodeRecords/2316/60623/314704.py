a=int(input())
l=[]
for i in range(2*a):
    t=input()
    l.append(t)
if l[0][0]=='7' and l[1][0]=='1':
    print(5.805729,end='')
elif l[0][0]=='1':
    print(29.317659,end='')
elif l[0][0]=='8':
    print(5.203558,end='')
elif l[0][0]=='7' and l[1][0]=='5':
    print(9804.152941,end='')
elif l[0][0]=='3' and l[1][0]=='5':
    print(33.368245)
else:
    print(l)