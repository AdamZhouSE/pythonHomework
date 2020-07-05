def solve():
    n,m=map(int,input().split())
    des=input().replace(' ','')
    now=input().replace(' ','')

    for i in range(1,n):
        for j in range(i+1,n):
            s1=now[:i]# len(s1)=i
            s2=now[i:j]# len(s2)=j-i
            s3=now[j:]# len(s3)=n-j

            if (not s1 in des) or (not s2 in des) or (not s3 in des):
                continue

            ps=[['1',str(i)],[str(i+1),str(j)],[str(j+1),str(n)]]
            ss=[s1,s2,s3]

            if ss[0]+ss[1]+ss[2]==des:
                print("YES")
                print(' '.join(ps[0]))
                print(' '.join(ps[1]))
                print(' '.join(ps[2]))
                return
            elif ss[0]+ss[2]+ss[1]==des:
                print("YES")
                print(' '.join(ps[0]))
                print(' '.join(ps[2]))
                print(' '.join(ps[1]))
                return
            elif ss[1]+ss[0]+ss[2]==des:
                print("YES")
                print(' '.join(ps[1]))
                print(' '.join(ps[0]))
                print(' '.join(ps[2]))
                return
            elif ss[1]+ss[2]+ss[0]==des:
                print("YES")
                print(' '.join(ps[0]))
                print(' '.join(ps[2]))
                print(' '.join(ps[1]))
                return
            elif ss[2]+ss[0]+ss[1]==des:
                print("YES")
                print(' '.join(ps[2]))
                print(' '.join(ps[0]))
                print(' '.join(ps[1]))
                return
            elif ss[2]+ss[1]+ss[0]==des:
                print("YES")
                print(' '.join(ps[2]))
                print(' '.join(ps[1]))
                print(' '.join(ps[0]))
                return
    print("NO")

if  __name__ == '__main__' :
    total=int(input())
    for _ in range(total):
        solve()