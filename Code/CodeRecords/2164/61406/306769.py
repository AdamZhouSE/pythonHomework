T = int(input())
for a in range(0,T):
    s = input()
    statistics=[]
    for i in range(0,26):
        statistics.append(0)
    for x in s:
        statistics[ord(x)-ord('a')]+=1
    kind = 26-statistics.count(0)
    print(len(s)-kind)
