def solve():
    n=int(input())
    s1=input()
    ss=[]
    for i in range(n-1):
        ss.append(input())

    t=l=len(s1)

    while l>0:
        for i in range(t-l+1):
            substr=s1[i:i+l]
            for s in ss:
                if not substr in s:
                    break
            else:
                print(l)
                return
        l-=1
    print(0)

if  __name__ == '__main__' :
    solve()