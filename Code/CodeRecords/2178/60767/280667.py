def getSpells(origin):
    length = len(origin)
    res = []
    for i in range(0,length):  #子串起始从0到length-1
        for j in range(1,length-i+1):  #子串长度
            temp = str(origin[i:i+j])
            if(temp not in res):
                res.append(temp)
    return len(res)

def getNum(origin):
    res = []
    for i in range(1,len(origin)+1):
        for x in getSpells(origin,i):
            if(x not in res):
                res.append(x)
    return res
n = int(input())
inp = input().split(" ")
nums = []
for i in inp:
    nums.append(int(i))
temp = []
for i in range(0,n):
    temp.append(nums[i])
    print(getSpells(temp))