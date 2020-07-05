if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        prod = input().split()
        s =set(prod)
        d={}
        for a in s:
            d[a]=prod.count(a)
        res = 0
        for item in d.items():
            if item[1]%2==0:
                res+=item[1]
            else:
                res+=item[1]-1
        print(res)