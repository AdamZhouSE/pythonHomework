n=int(input())
x=1
i=10
count=1
while x%n:
    x+=i
    i*=10
    count+=1
    if(x>100000):
        break

if(x>100000):
    print("-1")
else:

    print(count)
