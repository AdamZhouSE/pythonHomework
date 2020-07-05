def calculate(s1, s2):
    length = 0
    x = len(s1) - 1
    y = len(s2) - 1
    while x >= 0 and y >= 0:
        if s1[x] == s2[y]:
            length += 1
        else:
            break
        x -= 1
        y -= 1
    return length


list1 = input().split(" ")
m = int(list1[0])
n = int(list1[1])
oriString = input()
for i in range(n):
    listNum = input().split(" ")
    end1 = int(listNum[0])
    end2 = int(listNum[1])
    sunStrings = []
    for j in range(end1, end2+1):
        sunStrings.append(oriString[:j])
    result = 0
    for j in range(len(sunStrings)):
        for k in range(len(sunStrings)):
            if k != j:
                l = calculate(sunStrings[j], sunStrings[k])
                if l > result:
                    result = l
    print(result)
