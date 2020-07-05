number=eval(input())
string=input()
num=[int(n) for n in string.split()]
l1,l2=0,0
for i in num:
    if i==1:
        l1+=1
    else:
        l2+=1
if l1>l2:
    print(int(l2+(l1-l2)/3))
else:
    print(l1)
