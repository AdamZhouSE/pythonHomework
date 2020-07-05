def gcd(A, B):
    # A >= B
    if A < B:
        temp = A
        A = B
        B = temp
    while A % B != 0 and B % A != 0:
        if A % B != 0:
            A %= B
        if B % A != 0:
            B %= A
    return min(A, B)


N = eval(input())
A = eval(input())
B = eval(input())
res = []
gcd = gcd(A, B)
lcm = A * B // gcd
if gcd != 1 and (gcd == A or gcd == B):
    print(min(A, B) * N)
    exit()
incA = lcm // A
incB = lcm // B
eachInc = incA + incB - 1

single = [0]
for i in range(1, incA + 1):
    single.append(A * i)
for i in range(1, incB):
    single.append(B * i)
single.sort()
times = N // eachInc
remain = N % eachInc
print(lcm * times + single[remain])