count = int(input())
res = []
while True:
    try:
        ls = input()
        res.append(ls)
    except Exception as e:
        break
i = 0
able = 0
word1 = res[0][0]
word2 = res[0][1]
if word1 == word2:
    print("NO")
else:
    while i < count :
        if res[i][i] == res[i][count-1-i] and res[i][i] == word1:
            i+=1
        else:
            break
    if i != count:
        print("NO")
    else:
        for j in range(0,count):
            for h in range(0,count):
                if j == h or h == count-1-j:
                    continue
                if res[j][h] != word2:
                    able = 1
                    break
        if able:
            print("NO")
        else:
            print("YES")