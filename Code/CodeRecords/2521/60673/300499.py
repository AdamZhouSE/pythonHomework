from collections import Counter

inp = input()
barcodes = inp[1:len(inp)-1].split(",")
data = []
for i,j in Counter(barcodes).most_common():
    data += [i] * j
l = len(data)
res = [0] * l
res[::2] = data[:(l+1)//2]
res[1::2] = data[(l+1)//2:]
res = list(map(int, res))
print(res)