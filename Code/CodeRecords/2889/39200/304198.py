n = int(input())
sum = 0
s = input().split()
for x in s:
    sum += int(x)
print('{:6f}'.format(sum / n))
