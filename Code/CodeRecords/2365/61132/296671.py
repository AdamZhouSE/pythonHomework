n=int(input())
for i in range(n):
    m=input()
    l=input().split()
    l.sort(key=lambda x:x+x[-1],reverse=True)
    print(''.join(l))