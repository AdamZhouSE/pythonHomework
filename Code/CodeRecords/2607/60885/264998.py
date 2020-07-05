def isValid(s):
    counter = [0,0,0]
    for c in s:
        counter[ord(c)-ord('0')] += 1
    return counter[0] == counter[1] == counter[2]


def test():
    line = input()
    count = 0
    for i in range(1, len(line)+1):
        for j in range(0,len(line)-i+1):
            s = line[j:j+i]
            if isValid(s):
                count += 1
    A.append(count)

A = []
for i in range(int(input())):
    test()

for i in A:
    print(i)
