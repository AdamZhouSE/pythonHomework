class mystr:
    def __init__(self, string, index):
        self.string = string
        self.index = index


str1 = input()
str2 = input()
string1 = []
string2 = []
count = 0
for i in range(len(str1)):
    for j in range(i + 1, len(str1) + 1):
        string1.append(mystr(str1[i:j], i))
for i in range(len(str2)):
    for j in range(i + 1, len(str2) + 1):
        string2.append(mystr(str2[i:j], i))
for i in range(len(string1)):
    for j in range(len(string2)):
        if string1[i].string == string2[j].string and string1[i].index != string2[j].index:
            count += 1

print(count,end="")