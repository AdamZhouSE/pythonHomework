def smith(num):
    num=int(num)
    bound=num
    midnum=str(num)
    total=0
    for i in range(len(midnum)):
        total+=int(midnum[i])
    primesum=0
    i=2
    while i<=bound:
        if num%i==0:
            primesum+=i
            num=num/i
            i=2
        else:
            i=i+1
    if primesum==total:
        return 1
    elif bound==1 or bound==0:
        return 1
    else:
        return 0
        


t=int(input())
for i in range(t):
    num=input()
    answer=smith(num)
    print(answer)