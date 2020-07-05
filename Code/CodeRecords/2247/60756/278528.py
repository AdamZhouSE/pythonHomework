def maxIndex(a,b):
    return 0 if a>b else -1

stones=list(map(int,input().split(",")))
Alex=0
Lee=0
while stones:
    Alex+=stones.pop(maxIndex(stones[0],stones[-1]))
    Lee+=stones.pop(maxIndex(stones[0], stones[-1]))
print(Alex>Lee)