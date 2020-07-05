pasage = int(input())
store = []
for i in range(pasage):
    temp = input().split(" ")[1:]
    store.append(temp)
times = int(input())
for j in range(times):
    string = input()
    temp = []
    for k in range(len(store)):
        if string in store[k]:
            temp.append(k+1)
    if not temp:
        print(" ")
    else:
        for num in range(len(temp)):
            print(temp[num],"",end="")
        print("")

