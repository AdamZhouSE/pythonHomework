n=input()
n=int(n)
while n%4==0:
    n=n/4
if n>1:
    print("false")
else:
    print("true")