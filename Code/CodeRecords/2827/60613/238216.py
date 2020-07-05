NUM=int(input())
col=list(map(int,input().split()))
col.sort()
for i in range(NUM-1):
    print(col[i],end=" ")
print(col[NUM-1])