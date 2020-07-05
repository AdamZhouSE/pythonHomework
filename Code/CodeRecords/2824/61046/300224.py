inn = input().split()
test = input().split()

inn=list(map(int,inn))
num=inn[0]
t=inn[1]
c=inn[2]

test=list(map(int,test))

count=[]
for i in range(len(test)):
    if test[i]>t:
        count.append(i)
if count==[]:
    print(len(test)-c+1)
else:
    dict = []
    count.append(len(test))
    dict.append(count[0])
    for i in range(len(count)-1):
        dict.append(count[i + 1] - count[i]-1)
    res = []
    for x in dict:
        ans = 0
        if x < c:
            ans = 0
        elif x == c:
            ans = 1
        else:
            ans = x - c +1
        res.append(int(ans))
    print(sum(res))
