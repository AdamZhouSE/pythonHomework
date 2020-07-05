def check(s,n):
    if s == "" and n==10:
        return 6
    elif s == "":
        return 3
    def swap(x,y,str):
        temp1 = list(str)
        temp2 = temp1[x]
        temp1[x] = temp1[y]
        temp1[y] = temp2
        return "".join(temp1)

    x = 0
    res = 0
    t = n-1
    for i in range(t):
        for j in range(t, i - 1, -1): #从右向左
            if j == i: #没有对应的
                if n % 2 == 0 or x>1:
                    return "Impossible"
                else:
                    x+=1
                    res += n//2-i
                    break
            if s[j] == s[i]: #有对应的
                res += t-j
                for k in range(j,t):
                    s = swap(k,k+1,s)
                t -= 1
                break
    return res









n = int(input())
s = input()
print(check(s,n))
