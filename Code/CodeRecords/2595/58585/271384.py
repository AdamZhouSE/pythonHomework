num=int(input())
for i in range(num):
    N,K=map(int,input().split(" "))
    print(pow(K,N-1))