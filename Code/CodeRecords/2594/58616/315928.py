tests = int(input())
for i in range(tests):
    string =str(input())
    dct = {}
    max = -1
    for j in range(len(string)):
        if(dct.get(string[j]) == None):
            dct[string[j]] = j
        else:
            upd = j - dct[string[j]]
            if(upd > max):
                max= upd
    if(max == -1):
        print(max)
    else:
        print(max-1)