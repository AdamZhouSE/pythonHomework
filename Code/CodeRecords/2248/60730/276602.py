N = int(input())
A = int(input())
B = int(input())
m = min(A, B)
n = 0
while True:
    if m % A == 0 or m % B == 0:
        n = n + 1

        if n == N:
            break
        m = m + 1
    else:
        m = m + 1
print(m % (int(pow(10, 9)) + 7))
