
nq=input().split(' ')
n,q=int(nq[0]),int(nq[1])
dic=[]
for i in range(q):
    s=input().split(' ')
    if s[0]=='M':
        dic.append([int(s[2]),int(s[1])])
        dic.sort()
    else:
        age=int(s[2])
        y=int(s[1])
        found=False
        for j in range(len(dic)):
            if dic[j][0]>=age and dic[j][1]<=y:
                print(dic[j][0])
                found=True
                break
        if not found:
            print(-1)