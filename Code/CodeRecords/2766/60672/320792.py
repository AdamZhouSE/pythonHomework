t=int(input())
for i in range(t):
    n=int(input())
    answer=0
    if n%5==0:
        answer=-1
    else:
        answer=n%5
    print(answer)