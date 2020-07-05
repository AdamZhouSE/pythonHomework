t=int(input())
for nn in range(t):
    n=int(input())
    b=list(eval(input().replace(' ',',')))
    b=b.sort()
    if len(b)%2!=0:
        print(b[len(b)/2])
        