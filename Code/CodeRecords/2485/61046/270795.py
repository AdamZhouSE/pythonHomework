s = []
newList = []
num = int(input())
for i in range(num):
    m = input()
    temp = input()
    s.append(temp)

for i in range(num):
    temp = s[i].split(' ')
    count = {}
    res = ''
    for i in range(0,len(temp)):
        temp[i] = ''.join(sorted(str(temp[i])))
    for x in temp:
        if x in count:
            count[x] +=1
        else:
            count[x] = 1
    newcount = sorted(count.items(),key=lambda item:item[1])
    for key,value in newcount:
        res = res+str(value)+' '
    print(res.rstrip())