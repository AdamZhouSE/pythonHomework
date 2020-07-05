def cal(strs:list):
    for i in range(len(strs)):
        for j in range(i+1,len(strs)):
            if len(strs[i])<=len(strs[j]):
                if check(strs[i],strs[j]):
                    return True
    return False

def check(short,long):
    if short == long:
        return True
    for i in range(len(short)):
        if short[i] != long[i]:
            return False
    return True

strs = []
cur = 1
try:
    while True:
        temp = input()
        if temp == "9":
            if cal(strs):
                print("Set "+str(cur)+" is not immediately decodable")
            else:
                print("Set "+str(cur)+" is immediately decodable")
            strs = []
            cur+=1
        else:strs.append(temp)
except EOFError:
    pass