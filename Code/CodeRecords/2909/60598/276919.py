string = input()
N = len(string)
maxLetter = int(input())
minLength = int(input())
maxLength = int(input())


def check(sub):
    store = set()
    count = 0
    for s in range(len(sub)):
        if not sub[s] in store:
            store.add(sub[s])
            count += 1
            if count >maxLetter :
                return False
    return True


Max = 0
storeString = dict()
for i in range(minLength, maxLength+1):
    for j in range(N-i+1):
        temp = string[j:j+i]
        if check(temp):
            if temp in storeString:
                continue
            else:
                countS = 1
                for k in range(j+1, N-i+1):
                    if string[k:k+i] == temp:
                        countS += 1
                Max = max(Max, countS)
                storeString[temp] = countS
                countS = 1

print(Max)
