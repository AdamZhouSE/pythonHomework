n=int(input())
numbers=list(map(int,input().split(" ")))
numbers.sort()
i=len(numbers)-1
while i>=0:
    if numbers[i]<0:
        print(numbers[i])
        break
    a=numbers[i]**0.5
    b=int(a)
    if b*b!=numbers[i]:
        print(numbers[i])
        break
    i=i-1