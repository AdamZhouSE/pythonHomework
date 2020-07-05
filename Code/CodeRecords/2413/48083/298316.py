n = int(input())
start = int(input())

def circularPermutation(self, n: int, start: int):
    return [start, start ^ 1] if n == 1 else self.circularPermutation(n - 1, start) + self.circularPermutation(n - 1, start ^ 1 << n - 1)[::-1]
ans = circularPermutation(n,start)
print(ans)