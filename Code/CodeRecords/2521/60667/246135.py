import collections
barcodes = eval(input())
counter = dict(collections.Counter(barcodes))
sortedCounter = sorted( counter, key=lambda k: 0 - counter[k])
barcodes = []
for i in sortedCounter:
    barcodes += [i] * counter[i]
    arrangedBarcodes = [None for _ in range(len(barcodes))]
    arrangedBarcodes[::2] = barcodes[:len(arrangedBarcodes[::2])]
    arrangedBarcodes[1::2] = barcodes[len(arrangedBarcodes[::2]):]

print(arrangedBarcodes)