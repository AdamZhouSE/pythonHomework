numList = [int(x) for x in input().split(",")]
offset = int(input())
numList.sort()
offsetList  = []
# for i in range(0,len(numList)-1):
#     offsetList.append(numList[i+1]-numList[i])
#
# offsetList.sort()
# if(offsetList[min])
num2 = max(numList)-min(numList)
off = num2 - offset*2
if(off<=0):
    print(0)
else:
    print(off)