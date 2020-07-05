import math
def LCM(a, b):
    return a * (b // math.gcd(a, b))
N=int(input())
A=int(input())
B=int(input())
ab = LCM(A, B)
left = min(A, B)
right = N * B
while left < right:
    mid = (right + left) >> 1
    count = mid // A + mid // B - mid // ab
    if count < N:
        left = mid + 1
    else:
        right = mid
ans=left % (10 ** 9 + 7)
print(ans)