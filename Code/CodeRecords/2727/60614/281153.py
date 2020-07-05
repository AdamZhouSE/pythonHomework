for i in range(int(input())):
    num=int(input())
    mise=sorted([int(x) for x in input().split()])
    holes=sorted([int(x) for x in input().split()])
    maximum=0
    for j in range(num):
        maximum=max(abs(holes[j]-mise[j]),maximum)