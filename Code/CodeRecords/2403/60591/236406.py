total = eval(input())
members = eval(input())

result = []
for i in range(members):
    result.append(0)

now = 1
while(now > 0):
    situation = True
    for x in range(len(result)):
        if(now <= total):
            total -= now
            result[x] += now
            now += 1
        else:
            situation = False
            result[x] += total
            break
    if(not situation):
        break

result = list(map(str,result))
print("["+", ".join(result) + "]")