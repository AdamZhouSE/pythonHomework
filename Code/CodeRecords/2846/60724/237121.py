s=int(input())
numbers=input().split()
numbers=[int(x) for x in numbers]
for i in range(numbers.count(0)):
    numbers.remove(0)
res=set(numbers)
print(len(res))