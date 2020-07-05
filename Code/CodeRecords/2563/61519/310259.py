num=list(input())
num.pop(0)
num.pop(len(num)-1)
string="".join(num)
n=int(string)
k = 0
m = math.log((n+1)/2, 2)
i = int(m)
while i >= 2:
    a = n ** (1 / i)
    a = int(a)
    if (a ** (i + 1) == n * (a - 1) + 1):
        k = a
        break
    i -= 1
if (k == 0): k = n - 1
print(str(k))