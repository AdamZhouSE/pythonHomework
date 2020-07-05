
something = input()
dic = {}
word = []
for c in range(len(something)):
    dic.update({something[c:]:(c + 1)})
    word.append(something[c:])
word.sort()
for items in word:
    print(dic[items],end=" ")
print()