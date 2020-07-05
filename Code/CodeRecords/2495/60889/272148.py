def sort1(strings):
    newStrings = []
    for i in strings:
        loc = 0
        for j in newStrings:
            if len(i) > len(j):
                break
            loc = loc + 1
        newStrings.insert(loc,i)
    return newStrings

string = input()
strings = input().strip("[\"]").split("\",\"")
strings = sort1(strings)
for word in strings:
    i = 0
    j = 0
    while (i!=len(string)) and (j!=len(word)):
        if string[i] == word[j]:
            j = j + 1
        i = i + 1
    if j==len(word):
        output = word
        break
print(output)
            