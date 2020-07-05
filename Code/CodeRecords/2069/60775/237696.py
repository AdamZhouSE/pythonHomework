a = input()
b = input()
carry = 0
result = []
for i in range(len(a)+len(b)):
    result.append(0)

for x in range(1,len(b)+1):
    for i in range(len(a)-1,-1,-1):
        result[len(result)-x-(len(a)-i-1)] += ((ord(a[i])-ord("0"))*(ord(b[len(b)-x])-ord("0"))+carry )  #ord()可以获得ascii码
        carry = result[len(result)-x-(len(a)-i-1)] //10
        result[len(result) - x - (len(a) - i - 1)] %= 10
    result[len(result)-x-len(a)] += carry

strat = 0
for i in result:
    if i == 0:
        strat += 1
    else:
        break
re = ""
for i in result[strat:]:
    re = re + str(i)

print(re)