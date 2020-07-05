lines = []
while True:
    try:
        lines.append(input())
    except:
        break
buckets=int(lines.pop(0))
minutesToDie=int(lines.pop(0))
minutesToTest=int(lines.pop(0))
if(buckets == 1):
    print(0)
else:
    
    w = minutesToTest / minutesToDie + 1
    re = 1 
    while((w**re) < buckets):
        re=re+1

    print(re)