for n in range(int(input())):
    n=int(input())
    bi=bin(n)
    count=0
    for b in bi:
        if b=='1':count+=1
    print(count)