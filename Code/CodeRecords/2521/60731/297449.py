import collections
barcodes=eval(input())
counter=dict(collections.Counter(barcodes))
sortedCounter=sorted(counter,key=lambda k:0-counter[k])
barcodes=[]
for i in sortedCounter:
    barcodes+=[i]*counter[i]
res= [None for _ in range(len(barcodes))]
res[::2] = barcodes[:len(res[::2])]
res[1::2] = barcodes[len(res[::2]):]
print(res)