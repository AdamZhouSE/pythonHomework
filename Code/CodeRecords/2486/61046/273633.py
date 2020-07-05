num = input()
stringList = []
for i  in range(int(num)):
    stringList.append(input())

for i in range(int(num)):
    numstack = []
    charstack = []
    res = []
    fin =''
    test = list(stringList[i])
    for x in test:
        if x == '[':
            charstack.append(x)
        elif x == "1" or x == "2" or x == "3" or x == "4" or x == "5" or x == "6" or x == "7" or x == "8" or x=="9":
            numstack.append(x)
        elif x == ']':
            for s in reversed(charstack):
                if s == '[':
                    break
                if s != '[':
                    res.append(s)
                    charstack.pop()
            charstack.pop()
            count = numstack.pop()
            ans = ''.join(reversed(res))
            ans=ans*int(count)
            charstack.append(ans)
            res =[]
        else:
            charstack.append(x)
    print(ans)

