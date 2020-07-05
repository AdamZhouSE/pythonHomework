def allsubstring(s:str,begin,end):
    result = []
    for i in range(begin,end+1):
        result.append(s[0:i+1])
    return result

def getpre(s:str):
    result = []
    for end in range(len(s)):
        result.append(s[0:end+1])
    return result

def getpos(s:str):
    result = []
    for start in range(len(s)-1,-1,-1):
        result.append(s[start:])
    return result


input1 = input().split(' ')
slen = int(input1[0])
num_que = int(input1[1])
s = input()
for M in range(num_que):
    max1 = 0
    tmp = input().split(' ')
    start = int(tmp[0])
    end = int(tmp[1])
    events = allsubstring(s,start-1,end-1)
    pos = []
    for x in events:
        pos.append(getpos(x))
    for i in range(len(pos)-1):
        for j in range(i+1,len(pos)):
            for k in range(len(pos[i])):
                if pos[i][k] in pos[j]:
                    max1 = max(max1,len(pos[i][k]))
    print(max1)

