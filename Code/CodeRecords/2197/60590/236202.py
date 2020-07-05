tests = input()
tests = int(tests)

lists = []
for i in range(tests):
    n = input()
    n = int(n)
    lists.append(n)

lists1 = []
for i in range(lists.__len__()):
    temp = []
    for j in range(lists[i]):
        temp.append(j+1)
    lists1.append(temp)

def func(soldier = []):
    sword = []
    sword.append(1)
    for i in range(soldier.__len__()-1):
        sword.append(0)
    who = 0
    while sword.__len__() > 2:
        if who == sword.__len__() - 1:
            soldier.remove(soldier[0])
            sword.remove(sword[0])
            sword[0] = 1
            sword[1] = 0
            '''print("soldier:", end="")
            print(soldier)
            print("sword: ", end="")
            print(sword)'''
        else:
            soldier.remove(soldier[who + 1])
            temp = sword[who]
            sword.remove(temp)
            sword[who] = 0
            if who == sword.__len__()-1:
                sword[0] = 1
            else:
                sword[who + 1] = 1
            '''print("soldier:", end="")
            print(soldier)
            print("sword: ", end="")
            print(sword)'''
        who = sword.index(1)
        '''print("who: ",end="")
        print(who)'''
    '''print("soldier:", end="")
    print(soldier)
    print("sword: ", end="")
    print(sword)'''
    if soldier == [1]:
        print(1)
    else:
        survivor = sword.index(1)
        temp = soldier[1 - survivor]
        soldier.remove(temp)
        # print("survivor: ", end="")
        print(soldier[0])

for i in range(lists1.__len__()):
    func(lists1[i])
