k = int(input())
n = int(input())
res = n // k if k != 0 else 0
print(res)
if res == 0 and (k != 0 or n != 0):
    print(k, n)