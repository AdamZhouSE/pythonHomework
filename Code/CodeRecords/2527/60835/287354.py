group = eval(input())
vega = int(input())
price = int(input())
dis = int(input())
res = []
for n in group:
    if vega == 1:
        if n[2] == 1:
            if n[3] <= price and n[4] <= dis:
                res.append([n[1],n[0]])
    else:
        if n[3] <= price and n[4] <= dis:
            res.append([n[1],n[0]])
res.sort(reverse = True)
result = []
for n in res:
    result.append(n[1])
print(result)