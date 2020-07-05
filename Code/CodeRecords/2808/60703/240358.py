n = int(input());
listNum = [int(x) for x in input().split()];
MAX = max(listNum);
MIN = min(listNum);
maxIndex = listNum.index(MAX);
minIndex = listNum.index(MIN);
reslist = [];
if(maxIndex<minIndex):
    reslist.append(minIndex);
    reslist.append(len(listNum)-1-maxIndex);
else:
    reslist.append(maxIndex );
    reslist.append(len(listNum) - 1 - minIndex);
print(max(reslist));