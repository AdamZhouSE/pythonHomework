n = int(input())
count = 0
l = []

for i in range(1, n//2 + 2):
    if str(i).find('0') == -1 and str(n-i).find('0') == -1:
        count = i
        break

l.append(count)
l.append(n-count)

print(l)
