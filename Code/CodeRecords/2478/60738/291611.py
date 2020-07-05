n=int(input())
for i in range(n):
    num_list=list(map(int,input().split()))
    a=num_list[0]
    b=num_list[1]
    d=b-a
    N=int(input())
    print(str(a+d*(N-1)))