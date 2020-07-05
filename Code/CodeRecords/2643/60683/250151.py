customers = [int(x) for x in input().split(',')]
grumpy = [int(x) for x in input().split(',')]
X = eval(input())
sz = len(customers)
tempSum = 0
for i in range(sz):
    if grumpy[i] == 0:
        tempSum += customers[i]
slide = 0

for i in range(X):
    if grumpy[i] == 1:
        slide += customers[i]
left = 1
right = X
tempMax = slide
while right < sz:
    if grumpy[left - 1] == 1:
        slide -= customers[left - 1]
    if grumpy[right]==1:
        slide += customers[right]
    if slide > tempMax:
        tempMax = slide
    left += 1
    right += 1
print(tempMax + tempSum)