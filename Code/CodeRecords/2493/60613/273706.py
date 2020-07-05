num=int(input())
lst=list(map(int,input().split()))
NUM=int(input())

qa=[list(map(int,input().split())) for i in range(NUM)]
for i in qa:
    k=i[0]
    v=i[1]
    temp=lst[k-1:v]
    temp=set(temp)
    print(len(temp))