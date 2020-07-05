from collections import defaultdict
letters = input()
maxletters = int(input())
minsize = int(input())
maxsize = int(input())
dic = defaultdict(int)
for i in range(len(letters) - minsize + 1):
    c = letters[i: i + minsize]
    if len(set(c)) <= maxletters:
        dic[c] += 1
if dic:
    print(max(dic.values()))
else:
    print(0)