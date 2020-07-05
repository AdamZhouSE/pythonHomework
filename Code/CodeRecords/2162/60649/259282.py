d=input()
d=float(d)
k=int(input())
if k<0:
    k=-k
    d=1/d
res=1.0
for i in range(k):
    res*=d
print("{:.5f}".format(res))