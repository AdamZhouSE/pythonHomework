n=int(input())
for I in range(n):
    x=input()
    a=input().split()
    b=input().split()
    r="Yes"
    for i in b:
        if not i in a:
            r="No"
            break
    print(r)