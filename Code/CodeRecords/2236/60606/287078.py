n = int(input())
store = []
for i in range(n):
    line = input().split(" ")
    if line[0] == "1":
        store.append(int(line[1]))
        store.sort()
    elif line[0] == "2":
        store.remove(int(line[1]))
    elif line[0] == "3":
        print(store.index(int(line[1]))+1)
    elif line[0] == "4":
        print(store[int(line[1])-1])
    elif line[0] == "5":
        if len(store) == 1 and int(store[0]) < int(line[1]):
            print(store[0])
        else:
            sentinel = 0
            for i in range(len(store)):
                if int(store[i]) >= int(line[1]):
                    print(store[i-1])
                    sentinel = 1
                    break
            if int(store[len(store)-1]) < int(line[1]) and sentinel == 0:
                print(store[len(store)-1])
    else:
        if len(store) == 1 and int(store[0]) > int(line[1]):
            print(store[0])
        else:
            sentinel = 0
            for i in range(len(store)):
                if int(store[i]) > int(line[1]):
                    print(store[i])
                    sentinel = 1
                    break
            if int(store[len(store)-1]) > int(line[1]) and sentinel == 0:
                print(store[len(store)-1])