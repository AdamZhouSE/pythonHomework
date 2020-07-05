fox = input()
times = int(input())
inquiry = []
for i in range(times):
    temp = list(map(int, input().split(" ")))
    inquiry.append(temp)
#print(inquiry)
paper = []

str = ""
for i in range(fox.__len__()):
    if fox[i] == 'P':
        paper.append(str)
    elif fox[i] == 'B':
        str = str[0:str.__len__()-1]
    else:
        str += fox[i]
#print(paper)


def findSubString(text, target):
    times =0
    for i in range(text.__len__()):
        str = text[i : i+target.__len__()]
        if str == target:
            times += 1
    return times


res = []
for i in range(inquiry.__len__()):
    if inquiry[i][0] > paper.__len__() or inquiry[i][1] > paper.__len__():
        res.append(0)
    else:
        x = paper[inquiry[i][0] - 1]
        y = paper[inquiry[i][1] - 1]
        temp = findSubString(y, x)
        res.append(temp)
#print(res)

for i in range(res.__len__()):
    print(res[i])
