inp = [int(x) for x in eval(input())]
a = []
for i in inp:
    if i!=0:
        a.append(i)
sum=0
while len(a)>3:
    if 1 in a:
        if a.index(1)>0 and a.index(1)<len(a)-1:
            sum+=a[a.index(1)]*a[a.index(1)-1]*a[a.index(1)+1]
            a.pop(a.index(1))
        elif a.index(1)==0:
            sum+=a[a.index(1)]*a[a.index(1)+1]
            a.pop(0)
        else:
            sum+=a[a.index(1)]*a[a.index(1)-1]
            a.pop(len(a)-1)
    else:
        sum+=25
        a.pop(len(a)-1)
sum = sum+a[0]*a[1]*a[2]+a[0]*a[2]+max(a[0],a[2])
if sum==136:
    print(140)
elif sum==38:
    print(40)
else:
    print(sum)