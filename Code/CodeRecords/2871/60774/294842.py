n = int(input())
numLst = list(map(int,input().split(' ')))
groupOfTwo = numLst.count(2)
groupOfOne = numLst.count(1)
if(groupOfTwo <= groupOfOne):
    print(groupOfTwo + int((groupOfOne - groupOfTwo) / 3))
else:
    print(groupOfOne)