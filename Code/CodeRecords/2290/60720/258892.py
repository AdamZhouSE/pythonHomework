size=int(input())
for i in range(size):
    l=int(input())
    list1=input().split()
    for j in range(l-1):
        if list1[j+1]<list1[j]:
            print(list1[j+1],end=' ')
        else:
            print(-1,end=' ')
    print(-1,end=' ')
    print()
