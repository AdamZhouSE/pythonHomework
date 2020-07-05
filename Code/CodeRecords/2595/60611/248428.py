num = int(input())
for i in range(num):
    l=list(map(int,input().split()))
    page=l[1]**(l[0]-1)
    print(page)