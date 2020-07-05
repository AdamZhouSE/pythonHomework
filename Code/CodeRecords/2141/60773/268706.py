num=int(input())
for k in range(num):
    n=int(input())
    for i in range(n):
        s=bin(i+1)[2:]
        print(s,end=" ")
    print("")
        