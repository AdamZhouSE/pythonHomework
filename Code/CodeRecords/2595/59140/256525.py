T=int(input())
for i in range(0,T):
    example=input().split(" ")
    print(pow(int(example[1]),int(example[0])-1))