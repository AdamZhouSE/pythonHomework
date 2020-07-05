num=int(input())
for n in range(num):
    size=int(input())
    lst=list(input().split(' '))
    lst.sort()
    print(' '.join(lst))