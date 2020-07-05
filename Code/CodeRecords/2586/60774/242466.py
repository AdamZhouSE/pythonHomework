a = int(input())
b = int(input())
c = int(input())
step = [0,0]
numLst = sorted([a,b,c])
step[1] = numLst[2] - numLst[0] - 2
if(numLst[1] - numLst[0] > 2):
    step[0] = step[0] + 1
if(numLst[2] - numLst[1] > 2):
    step[0] = step[0] + 1
print(step)