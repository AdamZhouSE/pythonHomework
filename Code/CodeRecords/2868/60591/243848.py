n = eval(input())
nums = list(map(int,input().split(" ")))
dict = {}
for num in nums:
    if(num in dict):
        dict[num] += 1
    else:
        dict[num] = 1
keys = list(dict.keys())
min = n
for key in keys:
    now = 0
    for x in range(len(keys)):
        if((keys[x] - key) % 2 == 1):
            now += dict[keys[x]]
    if(now < min):
        min = now
print(min)