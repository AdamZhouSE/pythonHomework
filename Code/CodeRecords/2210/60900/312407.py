n = int(input())
target =[]
str =[]
for i in range(0,n):
    str.append(input())
    target.append(input())

for i in range(0,n):
    t = target[i]
    s = str[i]
    results =[]
    bb =[]
    for j in range(0,len(s)):
        result = ""
        st =j
        tt =0
        judge = -1
        while(st<len(s)):
            if judge ==1:
                results.append(result)
                bb.append(len(result))
                break
            judge =1
            result+=s[st]
            for o in range(0, len(t)):
                if t[o] not in result:
                    judge = -1
                    break
            if judge ==1:
                results.append(result)
                bb.append(len(result))
                break
            st+=1

    if len(results)!=0:
        print(results[bb.index(min(bb))])
    else:
        print(-1)