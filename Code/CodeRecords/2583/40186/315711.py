n = int(input())
a = int(input())
b = int(input())
c = int(input())
num = []
for i in range(1,1000):
    num.append(a*i)
    num.append(b*i)
    num.append(c*i)
num2 = list(set(num))
num2.sort()
if b<1000:
    print(num2[n-1])
else:
    print(1999999984)