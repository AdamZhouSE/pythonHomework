length = int(input())
strs = []
for i in range(length):
    str = input()
    adder = ""
    while(len(str)>0):
        adder = adder+max(str)*str.count(max(str))
        str = str.replace(max(str),"")
    strs.append(adder)
print(strs)
num = 0
while(len(strs)>0):
    temp = strs.count(strs[-1])
    things = strs[-1]
    print(strs,temp)
    for i in range(temp):
        strs.remove(strs[-1])
    num=num+1
print(num)