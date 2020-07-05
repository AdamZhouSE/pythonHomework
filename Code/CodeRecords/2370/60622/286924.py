N=int(input())
if N == 0:
    digits = ['0']
else:
    digits = []
    while N != 0:
        N, remainder = divmod(N, -2)
        if remainder < 0:
            N, remainder = N + 1, remainder + 2
        digits.append(str(remainder))
ans=''.join(digits[::-1])
print(ans)
