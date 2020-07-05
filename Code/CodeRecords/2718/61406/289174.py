string = input()
source = input().replace('[', '').replace(']', '').split(',')
pairs = []
for a in range(0, len(source) // 2):
    pair = []
    pair.append(int(source[2 * a]))
    pair.append(int(source[2 * a + 1]))
    pairs.append(pair)
for i in range(0,len(pairs)-1):
    for j in range(i+1,len(pairs)):
        if pairs[i][1]==pairs[j][1]:
            pairs.append([pairs[i][0],pairs[j][0]])
        elif pairs[i][0]==pairs[j][0]:
            pairs.append([pairs[i][1],pairs[j][1]])
        elif pairs[i][0]==pairs[j][1]:
            pairs.append([pairs[i][1],pairs[j][0]])
        elif pairs[i][1]==pairs[j][0]:
            pairs.append([pairs[i][0],pairs[j][1]])
previous = ""
while string != previous:
    previous = string
    for i in pairs:
        if string[i[0]] > string[i[1]] and i[0]<i[1]:
            char = string[i[1]]
            string = string[0:i[1]] + string[i[0]] + string[i[1] + 1:]
            string = string[0:i[0]] + char + string[i[0] + 1:]
        elif string[i[0]] < string[i[1]] and i[0] > i[1]:
            char = string[i[1]]
            string = string[0:i[1]] + string[i[0]] + string[i[1] + 1:]
            string = string[0:i[0]] + char + string[i[0] + 1:]
print(string)

