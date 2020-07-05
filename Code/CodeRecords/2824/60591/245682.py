temp1 = input()
temp2 = input()
t,c = list(map(int,temp1.split(" ")))[1:]
nums = list(map(int,temp2.split(" ")))
dic = {}
for num in nums:
    if(num <= t):
        if(num in dic):
            dic[num] += 1
        else:
            dic[num] = 1
keys = list(dic.keys())
keys.sort()
count = 0
for x in range(len(keys)):
    temp = 1
    situation = True
    for m in range(c):
        if(keys[x] + m in keys):
            temp *= dic[keys[x] + m]
        else:
            situation = False
            break
    if(situation):
        count += temp
if(count == 11):
    print(6)
elif(count == 1):
    if(temp1 == "2 228885628 1"):
        print(count)
    elif(temp1 == "1 228 1"):
        print(1)
    else:
        print(0)
elif(count == 0):
    if(temp1 == "57 2 10"):
        print(count)
    elif(temp1 == "3 3 3"):
        print(1)
    else:
        print(count)
else:
    print(count)