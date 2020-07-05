a=int(input())
b=input().split()
one=0
two=0
for i in range(a):
    b[i]=int(b[i])
mi=min(b)
ma=max(b)
b.remove(mi)
one=max(b)-min(b)
b.append(mi)
b.remove(ma)
two=max(b)-min(b)
if one>two:
    print(two)
else:
    print(one) 