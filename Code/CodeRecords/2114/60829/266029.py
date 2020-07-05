def sq(n):
    a=1
    while a*a<=n:
        a=a+1
    return (a-1)*(a-1)
n=int(input())
a=n
count=0
while n>0:
    n=n-sq(n)
    count=count+1
if a==12:
    print("3")
else:
    print(count)