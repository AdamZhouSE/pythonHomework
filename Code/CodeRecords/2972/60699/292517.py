cnt = int(input())
for i in range(cnt):
    strA = input()
    strB = input()
    if strA.__eq__(strB):
        print("Yes")
    elif len(strA) >= len(strB):
        print("No")
    else:
        lenA = len(strA)
        lenB = len(strB)
        start = 0
        startB = 0
        c = [-1, -1]
        while start < lenA and startB < lenB:
            if strA[start] == strB[startB]:
                if strA[start] != c[1]:
                    temp = c[1]
                    c[1] = strA[start]
                    c[0] = temp

                start += 1
                startB += 1
            else:
                if start == 0:
                    break
                if strA[start - 1] == strB[startB]:
                    if strB[startB] != c[0] and c[0] != -1:
                        startB += 1
                    else:
                        break
                elif strA[start - 1] != strB[startB]:
                    startB += 1
        if start == lenA:
            if startB==lenB:
                print("Yes")
            else:
                flag=False
                for j in range(startB,lenB):
                    if strB[j]==strA[lenA-1]:
                        flag=True
                if flag:
                    print("No")
                else:
                    print("Yes")
                        
        else:
            print("No")