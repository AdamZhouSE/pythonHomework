t = int(input())
for i in range(t):
    n = int(input())
    begin = 1
    while begin**3<=n:
        begin+=1
    print(begin-1)
    