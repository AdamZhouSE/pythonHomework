k=int(input())
for qqq in range(0,k):
    n=int(input())
    rope=list(map(int,input().split()))
    rope.sort()
    total=0
    while len(rope)>1:
        csum=rope[0]+rope[1]
        total+=csum
        rope=rope[2:]
        rope.append(csum)
        rope.sort()
    print(total)