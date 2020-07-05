n=int(input())
l=list(map(int,input().split()))
all=sum(l)
turn=1
s=0
while l!=[]:
    if l[0] > l[-1]:
        tmp = l.pop(0)
        if turn:s+=tmp
    else:
        tmp = l.pop()
        if turn:s+=tmp
    turn=1-turn
print(' '.join([str(s),str(all-s)]))