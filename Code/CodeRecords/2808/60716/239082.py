num = int(input())
str = input().split(' ')
words = [ int(i) for i in str]
minplace = words.index(1)+1
maxplace = words.index(num)+1

toone =0
tonum = 0
differ = abs(minplace - maxplace)
if minplace<maxplace:
    tozero = minplace -1
    tonum = num - maxplace
else:
    tozero = maxplace-1
    tonum = num - minplace
if tozero>=tonum:
    print(tozero+differ)
else:
    print(tonum+differ)