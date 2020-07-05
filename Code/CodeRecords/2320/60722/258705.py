string=input()
k=int(input())
character=[]
for i in range(len(string)):
    character.append(string[i])
if k>=2:
    character.sort()
    result=""
    for i in range(len(character)):
        result+=character[i]
    print(result)
else:
    while character[0]!=min(character):
        character.append(character[0])
        character.remove(character[0])
    result = ""
    for i in range(len(character)):
        result += character[i]
    print(result)