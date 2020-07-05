nums = input().split(",")
threshold = int(input())
numSum = 0
for i in nums:
    j = int(i)
    numSum = numSum + j
minDiv = int(numSum/threshold)
div = minDiv
judge = True
while judge:
    quotientSum = 0
    for i in nums:
        j = int(i)
        quotientSum = quotientSum + int(j/div)
        if j%div != 0:
            quotientSum = quotientSum + 1
    if quotientSum <= threshold:
        judge = False
    else:
        div = div + 1
print(div)
