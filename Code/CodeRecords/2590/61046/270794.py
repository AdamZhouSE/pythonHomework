s = []
newList = []
num = int(input())
for i in range(num):
    temp = input()
    s.append(temp)

for i in range(num):
    temp = list(sorted(s[i]))
    count = {}
    res = ''
    for x in temp:
        if x in count:
            count[x] +=1;
        else:
            count[x] = 1
    newcount = sorted(count.items(),key=lambda item:item[1])
    for key,value in newcount:
        if value == 1 or key == 'a' or key == 'e' or key =='i' or key=='o' or key=='u' :
            res += key

    if len(res) % 2 ==1:
        print("HE!")
    else:
        print("SHE!")