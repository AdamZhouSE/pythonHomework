n,h=map(int,input().split(' '))
a=list(map(int,input().split(' ')))
for ai in a:
    if ai>h:
        n+=1
print(n)