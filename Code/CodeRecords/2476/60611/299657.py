num=int(input())
for i in range(num):
    n=int(input())
    t=sorted(list(map(int,input().split(" "))))
    count=0
    for _ in range(n-1):
        a=t[0]+t[1]
        count+=a
        t=t[2::]
        if t:
            for j in range(len(t)):
                if a<t[j]:
                    t.insert(j,a)
                    break
            if a>t[len(t)-1]:
                t.append(a)
    print(count)