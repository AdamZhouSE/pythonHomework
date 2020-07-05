line=[int(x) for x in input().split()]
n=line[0]
m=line[1]
finalwinner=[0]*(n+1)
for i in range(m):
    line = [int(x) for x in input().split()]
    tmpwinner=line.index(max(line))+1
    finalwinner[tmpwinner]+=1
print(finalwinner.index(max(finalwinner)))