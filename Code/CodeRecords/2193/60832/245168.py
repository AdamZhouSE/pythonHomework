get = input().split(" ")
length = int(get[0])
num = int(get[1])
history = input()

for i in range(0, num):
    degree = 0
    temp = input().split(" ")
    start = int(temp[0])
    end = int(temp[1])

    for j in range(start,end+1):
        sth=history[:j]
        for k in range(j+1,end+1):
            cmp=history[:k]
            t=0
            len1=len(sth)
            len2=len(cmp)
            for x in range(1,j+1):
                if sth[len1-x]==cmp[len2-x]:
                    t+=1
                else:
                    break

            if t>degree:
                degree=t

    print(degree)
