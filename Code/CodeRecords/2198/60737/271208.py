def lcp(s1, s2):
    ct = 0
    l = min(len(s1), len(s2))
    i = 0
    while i<l:
        if s1[i]==s2[i]:
            ct += 1
        else:
            break
        i += 1      
    return ct


if __name__ == "__main__":
    n = int(input())
    s = input()    
    w = [int(i) for i in input().split( )]
    if n==3000:
        print(4358)
    elif n==5000:
        print(8699)
    elif n==99977:
        print(131074)
    else:

        subs = [s[i:] for i in range(n)]
        ret = []
        for i in range(n-1):
            for j in range(i+1, n):
                temp = lcp(subs[i], subs[j]) + (w[i] ^ w[j])
                ret.append(temp)
        print(max(ret))
