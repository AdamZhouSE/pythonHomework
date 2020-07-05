tem = input().split('"')
trickets = []
n = 0
while n < len(tem):
    if n % 2 == 1:
        tem2 = [tem[n]]
        n = n + 2
        tem2.append(tem[n])
        trickets.append(tem2)
    n = n + 1
#print(trickets)
result = ["JFK"]
now = "JFK"
trickets.sort()
while len(trickets) != 0:
    for n in trickets:
        if n[0] == now:
            now = n[1]
            #print(n)
            result.append(now)
            trickets.remove(n)
            break
print(result)