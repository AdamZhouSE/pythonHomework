num = input()
i = 0
compDict = {'A':2, 'B':2, 'C':2, 'D':3, 'E':3, 'F':3, 'G':4, 'H':4, 'I':4, 'J':5, 'K':5, 'L':5, 'M':6, 'N':6, 'O':6, 'P':7, 'R':7, 'S':7, 'T':8, 'U':8, 'V':8, 'W':9, 'X':9, 'Y':9}
phoneList = []
while i < int(num):
    phoneList.append(input())
    i = i + 1
i = 0
phoneDict = {}
while i < len(phoneList):
    phoneList[i] = phoneList[i].replace('-', '')
    temp_list = list(phoneList[i])
    temp_list.insert(3, '-')
    phoneList[i] = ''.join(temp_list)
    for ch in phoneList[i]:
        if ch.isalpha():
            phoneList[i] = phoneList[i].replace(ch, str(compDict[ch]))
    if phoneList[i] in phoneDict.keys():
        phoneDict[phoneList[i]] = phoneDict[phoneList[i]] + 1
    else:
        phoneDict[phoneList[i]] = 1
    i = i + 1
for key in list(phoneDict.keys()):
    if phoneDict[key] == 1:
        del phoneDict[key]
if not bool(phoneDict):
    print('No duplicates.', end = '')
else:
    for elem in phoneDict:
        print('{} {}'.format(elem, phoneDict[elem]))