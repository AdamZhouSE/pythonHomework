def allsubstring(s:str,begin,end):
    result = []
    for i in range(begin,end+1):
        result.append(s[0:i+1])
    return result

def longest_commom_post(sa,sb):
    length = max(len(sa),len(sb))
    max1 = 0
    for i in range(1,length+1):
        if sa[len(sa)-i:] == sb[len(sb)-i:]:
            max1 = i
    return max1


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
    for i in range(len(events)-1):
        for j in range(i+1,len(events)):
            max1 = max(max1,longest_commom_post(events[i],events[j]))

    print(max1)

