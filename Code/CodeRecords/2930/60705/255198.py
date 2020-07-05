n = int(input())
l = list(map(int, input().split(" ")))
count = 0
for i in range(1, n-1):
    if (l[i] < l[i+1] and l[i] < l[i-1]) or (l[i] > l[i+1] and l[i] > l[i-1]):
        count += 1 
print(count)