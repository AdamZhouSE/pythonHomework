cnt=int(input())
for i in range(0,cnt):
    list1=list(map(int,input().split(' ')))
    print(list1[1]*((list1[0]+1)//2))