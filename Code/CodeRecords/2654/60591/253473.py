n = eval(input())
sets = {}
result = []
for x in range(100):
    result.append(0)
while(n != 0):
    n -= 1
    op = list(map(int,input().split(" ")))
    sets[(op[0],op[1])] = op[2]

keys = list(sets.keys())
for key in keys:
    for x in range(key[0],key[1]):
        if(result[x] < sets[key]):
            result[x] = sets[key]
print(sum(result))