def isValid(nums,total,C):
    result = []
    for x in range(total):
        result.append(0)
    for num in nums:
        for x in range(num[0] - 1,num[1]):
            result[x] += 1
    for x in range(len(result)):
        if(result[x] > C[x]):
            return False
    return True

def generate(length,now,result,path):
    if(length == 0):
        path.sort()
        if(path not in result):
            result.append(path)
        return
    if(length > len(now)):
        return
    for x in now:
        temp = path.copy()
        temp.append(x)
        res = now.copy()
        res.remove(x)
        generate(length - 1,res,result,temp)

def find(AB,total,C):
    for x in range(len(AB)):
        result = []
        path = []
        generate(len(AB) - x, AB, result, path)
        for res in result:
            if (isValid(res, total, C)):
                return len(AB) - x
    return -1

N,M = list(map(int,input().split(" ")))
AB =[]
C = []
total = N
while(N != 0):
    N = N - 1
    C.append(eval(input()))

while(M != 0):
    M = M - 1
    string = input().strip()
    temp = list(map(int,string.split(" ")))
    AB.append(temp)

print(find(AB,total,C))