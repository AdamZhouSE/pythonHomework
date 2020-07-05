num=int(input())
for m in range(num):
    N=int(input())
    nums=list(map(int,input().split(" ")))
    K=int(input())
    print(sorted(nums)[K-1])
