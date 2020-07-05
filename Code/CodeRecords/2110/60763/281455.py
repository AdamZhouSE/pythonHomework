n = int(input())
# print("{} =".format(n),end=' ')
s = []
while n>1:
    for i in range(2,n+1):
        if n%i==0:
            n=int(n/i)
            s.append(i)
for i in range(s.count(3)):
    s.remove(3)
for i in range(s.count(2)):
    s.remove(2)
for i in range(s.count(5)):
    s.remove(5)
if n == 1 or len(s) == 0:
    print(True)
else:
    print(False)