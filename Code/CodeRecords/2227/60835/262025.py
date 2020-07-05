n = int(input())
k = int(input())
seen = set()
res = []
def find(string):
    for x in range(k):
        tem = string + str(x)
        if tem not in seen:
            seen.add(tem)
            find(tem[1:])
            res.append(str(x))
    #print(res)
find('0'*(n-1))
res.reverse()
print(''.join(res) + '0'*(n-1))