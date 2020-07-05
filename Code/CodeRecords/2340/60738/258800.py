n=int(input())
for i in range(n):
    a=int(input())
    num_list=list(map(int,input().split()))
    start=num_list[0]
    value=0
    for j in range(1,a):
        if num_list[j]>=start:
            start=num_list[j]
        else:
            value+=start-num_list[j]
    print(value)
    