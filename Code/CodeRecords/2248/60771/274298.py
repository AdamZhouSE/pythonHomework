#30
N = int(input())
A = int(input())
B = int(input())
count = 0
num = 1
while count < N:
    if num % A == 0 or num % B == 0:
        count += 1
    num += 1
print(num-1)
