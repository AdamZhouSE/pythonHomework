n=int(input())
before=input().split()
after=input().split()
dis=0
for i in range(0,n-1):
    for j in range(i+1,n):
        if before.index(after[i])>before.index(after[j]):
            dis+=1
print(dis)