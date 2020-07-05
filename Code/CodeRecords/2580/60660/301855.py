n=int(input())
m=int(input())
t=int(input())
mx,my=n,m
for _ in range(t):
    l=eval('[' + input()+ ']')
    mx=min(mx,l[0])
    my=min(my,l[1])
print(mx*my)