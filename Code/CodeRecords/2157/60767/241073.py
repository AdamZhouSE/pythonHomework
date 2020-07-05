dict = {"M":1000, "D":500, "C":100, "L":50, "X":10 ,"V":5, "I":1}
Rome = input()
res = 0
for x in range(0,len(Rome)-1):
    if(dict[Rome[x]]>=dict[Rome[x+1]]):
        res = res + dict[Rome[x]]
    else:
        res = res - dict[Rome[x]]
res += dict[Rome[len(Rome)-1]]
print(res)
    