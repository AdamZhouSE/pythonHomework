from collections import Counter

tmp = list(map(int, input().split(",")))
dict = Counter(tmp)
ans = 0
for key in dict:
    test = int((dict[key]-1)/key)
    ans += ((int((dict[key]-2)/key))+1)*(key+1)
print(ans)
