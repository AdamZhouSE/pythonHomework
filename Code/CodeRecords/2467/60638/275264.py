n=int(input())
for x in range(0,n):
    k=list(map(int,input().split(" ")))[2]
    s=input()
    s=s+" "+input()
    numbers=list(map(int,s.split(" ")))
    numbers.sort()
    print(numbers[k-1])