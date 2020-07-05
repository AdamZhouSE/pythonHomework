n=int(input())
for i in range(n):
    m=input()
    l=input().split()
    l.sort(reverse=True)
    print(''.join(l))