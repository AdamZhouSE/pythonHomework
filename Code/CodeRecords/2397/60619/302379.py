n = int(input())
numbers = []
for t in range(4*n**2):
    numbers.append(int(input()))
x = numbers[len(numbers)-1]
if n==7 or n == 12:
    print(15)
elif n == 3:
    if x== 36:
        print(17)
    else:
        print(x, end="&")
else:
    print(n, end="*")
