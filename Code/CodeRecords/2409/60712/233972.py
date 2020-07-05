inp = input()
inp = inp.split(",")
chips = []
mix = 999999
for i in range(len(inp)):
    chips.append(int(inp[i]))
for i in range(len(chips)):
    sum=0
    for j in range(len(chips)):
        sum = sum + (abs(chips[i]-chips[j]))%2
    if sum<mix:
        mix=sum
print(mix)