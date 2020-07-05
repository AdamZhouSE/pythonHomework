piles = list(eval(input()))
re = [0, 0]
count = 0
while len(piles) > 0:
    if piles[0] > piles[-1]:
        re[count % 2] += piles[0]
        del piles[0]
    else:
        re[count % 2] += piles[-1]
        del piles[-1]
    count += 1
print(re[0] > re[1])