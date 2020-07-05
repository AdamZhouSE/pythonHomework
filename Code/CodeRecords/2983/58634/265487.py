def check(s,n):
    def swap(x,y,str):
        temp1 = list(str)
        temp2 = temp1[x]
        temp1[x] = temp1[y]
        temp1[y] = temp2
        return "".join(temp1)

    hasOneSingle = False
    res = 0
    m = n-1
    for i in range(m):
        for j in range(m, i - 1, -1):
            if (j == i):
                if n % 2 == 0 or hasOneSingle:
                    print("No")
                    return -1
                hasOneSingle = 1
                res +=n//2-i
            elif s[j]==s[i]:
                for k in range(j,m):
                    s = swap(k,k+1,s)
                    res+=1
                m-=1
                break
    return res


n = int(input())
s = input()
print(check(s,n))
