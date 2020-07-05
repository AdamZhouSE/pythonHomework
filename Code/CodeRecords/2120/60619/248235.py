n = int(input())
area = []
for i in range(2, n+1):
    x = int(n/i)
    t = n % i
    area.append((x+1)**t * x**(i-t))
area.sort()
print(area[len(area)-1])