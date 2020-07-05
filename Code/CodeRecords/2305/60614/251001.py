fInput=[int(x) for x in input().split()]
points=fInput[0]
colors=fInput[1]
numOfAlice=int(input())
alice=[]
for i in range(numOfAlice):
    alice.append([int(x) for x in input().split()])
numOfShinobu=int(input())
shinobu=[]
for i in range(numOfShinobu):
    shinobu.append([int(x) for x in input().split()])
def exe(hand,opponent,reference):
    if len(hand)==1:
        if hand[0][0]==reference[0] or hand[0][1]==reference[1]:
            return True
        else:
            return False
    for j in hand:
        if j[0]==reference[0] or j[1]==reference[1]:
            temp=[]+hand
            temp.remove(j)
            judge=not exe(opponent,temp,j)
            if judge:
                return True
    return False
for i in alice:
    temp=[]+alice
    temp.remove(i)
    if exe(shinobu,temp,i):
        print(1)
    else:
        print(0)