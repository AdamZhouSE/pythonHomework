n=int(input())
for i in range(n):
    num_list=list(map(int,input().split()))
    num=num_list[0]
    string=str(bin(num))
    a=num_list[1]
    b=num_list[2]
    for j in range(a-1,b):
        if (string[-(j+1)]!="1"):
            num+=2**j
    print(num)