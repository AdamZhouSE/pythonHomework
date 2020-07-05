tests = input()
tests = int(tests)

lists = []
for i in range(tests):
    num = input()
    num = int(num)
    lists.append(num)

for i in range(lists.__len__()):
    print()
    if i!=0:
        print()
    for j in range(lists[i]):
        temp = j+1
        if temp == lists[i]:
            print(str(temp), end="")
        else:
            print(str(temp)+" ", end="")