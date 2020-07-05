n=eval(input())
rec=[1]
if n==1:
    print(False)
    exit()
for i in range(2,n):
    if n%i==0:
        rec.append(i)
if sum(rec)==n:
    print(True)
else:
    print(False)