n=int(input())
for x in range(0,n):
    numbers=list(map(int , input().split(" ")))
    print(numbers[1]-1-numbers[0])