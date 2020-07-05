a=int(input())-1
n=list(map(int,input().split()))
for i in range(a):
    if i%2==0:
        n.remove(max(n))
    else:
        n.remove(min(n))
print(n[0])