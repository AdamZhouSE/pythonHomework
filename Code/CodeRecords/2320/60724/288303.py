string=input()
2
k=int(input())
3
character=[]
4
for i in range(len(string)):
5
    character.append(string[i])
6
if k>=2:
7
    character.sort()
8
    result=""
9
    for i in range(len(character)):
10
        result+=character[i]
11
    print(result)
12
else:
13
    while character[0]!=min(character):
14
        character.append(character[0])
15
        character.remove(character[0])
16
    result = ""
17
    for i in range(len(character)):
18
        result += character[i]
19
    print(result)