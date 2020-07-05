n=int(input())
num_list=list(map(int,input().split()))
k=int(input())
number=list(map(int,input().split()))
for i in range(k):
    for j in range(n-1):
        if number[i]>=sum(num_list[:j]) and number[i]<=sum(num_list[:j+1]):
            print(j+1)
            break