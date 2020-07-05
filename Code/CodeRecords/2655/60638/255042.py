n=int(input())
for x in range(0,n):
    num=int(input())
    exp=0
    while pow(2,exp)<num:
        exp=exp+1
    print(pow(2,exp))