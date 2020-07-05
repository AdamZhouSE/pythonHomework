n=int(input())
for x in range(0,n):
    inpu=input()
    numbersA=list(map(int,input().split(" ")))
    numbersB=list(map(int,input().split(" ")))
    sum=0
    for i in range(0,len(numbersB)):
        sum=sum+max(numbersA[i],numbersB[i])
    print(sum)