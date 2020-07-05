numbers = list(map(int,input().split(',')))
for i in set(numbers):
    if numbers.count(i)>len(numbers)/2:
        print(i)
        break