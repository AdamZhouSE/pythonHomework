s = input()
box = []
ad = []
s = list(s)
s.sort()
for i in range(len(s) - 1):
    ad.append(s[i])
    if s[i] != s[i + 1]:
        box.append(ad)
        ad = []
ad.append(s[i + 1])
box.append(ad)
length = [len(e) for e in box]
if max(length) - 1 > sum(length) - max(length):
    print('')
else:
    string = []
    while len(string) != len(s):
        for i in range(len(box)):
            if len(box[i]) != 0:
                string.append(box[i][0])
                box[i].pop(0)
    # if string[len(string) - 1] == string[len(string) - 2] and string[len(string) - 1] == string[0]:
    #     print('')
    print(''.join(string))