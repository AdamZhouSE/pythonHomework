n = int(input())
operations = list(map(int, input().split()))
#print(operations)

subSpell = []
for i in range(operations.__len__()):
    spell = operations[0:i+1]
    #print(spell)
    arr = []
    for j in range(spell.__len__()+1):
        for k in range(j+1, spell.__len__()+1):
            if not arr.__contains__(spell[j:k]):
                arr.append(spell[j:k])
    #print(arr)
    subSpell.append(arr.__len__())

#print(subSpell)
for i in range(subSpell.__len__()):
    print(subSpell[i])