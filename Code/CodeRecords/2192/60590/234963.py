tests = input()
tests = int(tests)

def func(num):
    temp = []
    n=num
    while(True):
        temp.append(num)
        if (num > 0):
            num = num - 5
        elif (num < 0 or num==0):
            while(num!=n):
                num = num +5
                temp.append(num)
            #print(temp)
            break

    for i in range(temp.__len__()):
        print(str(temp[i])+" ", end="")
    print()

lists = []
for i in range(tests):
    num = input()
    num = int(num)
    lists.append(num)

for i in range(lists.__len__()):
    func(lists[i])
