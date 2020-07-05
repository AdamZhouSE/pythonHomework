# 18
inp = input()
inp = input()
a = inp.split()
for i in range(len(a)):
    a[i] = int(a[i])
n = len(a)
for i in range(len(a)):
    while(a[i]%2==0):
        a[i]/=2
    while(a[i]%3==0):
        a[i]/=3
ff=1
for i in range(n-1):
    if(a[i]!=a[i+1]):
        ff=0
        break
if ff == 1:
    print("Yes")
else:
    print("No")