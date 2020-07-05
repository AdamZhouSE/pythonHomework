def gcd(a,b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)


t = int(input())
for i in range(t):
    n = int(input())
    nums = [int(i) for i in input().split(" ")]
    print(int(max(nums)*min(nums)/gcd(max(nums),min(nums))))