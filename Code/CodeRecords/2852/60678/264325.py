n = int(input())
socies = input().split()

imfo = []
tempforCMP = socies[0]
count = 0
for i in range(0, n):
    if socies[i] != tempforCMP:
        imfo.append(count)
        count = 1
        tempforCMP = socies[i]
        continue
    count += 1
imfo.append(count)

max = 0
for i in range(0, len(imfo) - 1):
    # sum = imfo[i] + imfo[i + 1]
    sum = 2 * min(imfo[i], imfo[i + 1])
    if max < sum:
        max = sum
print(max)