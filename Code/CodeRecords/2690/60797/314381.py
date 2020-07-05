if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        [n,m] = [int(a) for a in input().split()]
        [s,t] = input().split()
        d = {}
        p=0
        for ch in t:
            d[ch]=p
            p+=1
        p = 0
        count =0
        for i in range(len(s)):
            if s[i]==t[p]:
                p += 1
                continue
            else:
                p=d.get(s[i],default=0)
                count +=1
        print(count)
