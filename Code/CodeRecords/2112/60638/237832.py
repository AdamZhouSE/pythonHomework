numbers=list(map(int,input().split(",")))
numbers.sort()
for i in range(0,len(numbers)-1):
    if numbers[i+1]-numbers[i]==2:
        print(numbers[i]+1)
        break