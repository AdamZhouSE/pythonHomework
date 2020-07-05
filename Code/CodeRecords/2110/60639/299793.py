n=int(input())
list=[2,3,5]
for i in list:
    while n%i==0:
        n=n/i
if n==1:
    print(True)
else:
    print(False)