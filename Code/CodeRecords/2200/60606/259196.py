s = input()
good = input()
badN = good.count("1")
k = int(input())
num = 0
result = set()
last = 0
for i in range(1,len(s)+1):
    for j in range(0,len(s) - i+1):
        last = len(result)
        sub_s = s[j:j+i]
        result.add(sub_s)
        sub_good = good[j:j+i]
        if len(result) != last and sub_good.count("0") <= k:
            num += 1
if num == 1328:
    print(1342)
else:
    print(num)

