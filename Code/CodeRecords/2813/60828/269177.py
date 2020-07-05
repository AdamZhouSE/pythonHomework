def h27():
    n = int(input())
    dic = {}
    nameRec = []
    scoreRec = []
    for i in range(n):
        s = input().split()
        name = s[0]
        score = int(s[1])
        nameRec.append(name)
        scoreRec.append(score)
        if(name in dic):
            dic[name] += score
        else:
            dic[name] = score
    Max = 0
    for key,value in dic.items():
        Max = max(value,Max)
    for key,value in dic.items():
        if(value<Max):
            dic[key] = "invalid"
        else:
            dic[key] = 0
    temp = {}
    for i in range(n):
        key = nameRec[i]
        if(dic[key]!="invalid"):
            dic[key] += scoreRec[i]
            if(dic[key]>=Max):
                print(key)
                break

if __name__ == '__main__':
    h27()