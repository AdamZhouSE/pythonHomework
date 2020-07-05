p, n = map(int, input().split(' '))
numbers = []
for i in range(n):
    numbers.append(int(input()) % p)
for index in range(len(numbers)):
    if numbers[index] in numbers[:index]:
        print(index+1)
        break
    if index == len(numbers)-1:
        print(-1)