n=int(input())
for x in range(0,n):
    num=int(input())
    numbers=list(map(int,input().split(" ")))
    k=int(input())
    numbers.sort()
    print(numbers[k-1])