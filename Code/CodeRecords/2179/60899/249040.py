length,num = map(int,input().split())
s = input()
for i in range(num):
    prelen = 0
    q = list(map(int,input().split()))
    a,b,c,d = q[0]-1,q[1]-1,q[2]-1,q[3]-1
    #print(len(s[a:b]))
    print(min(len(s[a:b+1]),len(s[c:d+1])))
    for j in range(min(len(s[a:b+1]),len(s[c:d+1]))):
        if(s[a:a+j+1]==s[c:c+j+1]):
            prelen += 1
        else:
            print(prelen)
            break

