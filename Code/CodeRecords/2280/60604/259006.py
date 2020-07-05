n=int(input())
for I in range(n):
    l=input()
    a=input().split()
    for i in range(len(a)):
        if i+1!=int(a[i]):
            print(i+1)
            break