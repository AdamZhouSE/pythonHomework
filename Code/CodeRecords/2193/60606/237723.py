def find(s1,s2):
    sentinel = 0
    s1 = list(s1)
    s2 = list(s2)
    s1.reverse()
    s2.reverse()
    while sentinel<len(s1) and sentinel<len(s2):
        if s1[sentinel] == s2[sentinel]:
            sentinel += 1
        else:
            break
    return sentinel
line1 = input().split(" ")
n = int(line1[0])
m = int(line1[1])
s = input()
for i in range(m):
    length = 0
    result = []
    line = input().split(" ")
    for j in range(int(line[1]) - int(line[0]) + 1):
        result.append(s[:int(line[0])+j])
    for k in range(len(result)):
        for l in range(k+1,len(result)):
            temp = find(result[k],result[l])
            if temp > length:
                length = temp
    print(length)



#0001110011111111111010011111011100111111110011100111111111110101111111100111001111111110011111110101

#30 31


