cases=int(input())
for i in range(cases):
    n=int(input())
    expo=0
    if n % 2==0:
        expo=pow(3,n//2-1)
    if n % 2!=0:
        expo=pow(2,n//2)
    print(pow(2,expo))