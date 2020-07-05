n = int(input())
for j in range(n):
    n = int(input())
    l=list(input())
    for i in l:
        if l.count(i)==1:
            print(i)
            break
    else:
        print(-1)