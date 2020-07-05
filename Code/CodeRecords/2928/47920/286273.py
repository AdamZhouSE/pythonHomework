v = int(input())
li = input().split(' ')
temp = []
for i in li:
    temp.append(int(i))
#print(temp)
if(v < min(temp)):
    print('-1')
else:
    ind1 = temp.index(min(temp))
    _min1 = min(temp)
    temp.pop(ind1)
    _min2 = min(temp)
    ind2 = temp.index(_min2)
    if(_min1 == _min2):
        print(str(ind2+1) * int((v/_min1)))
    else:
        print(str(ind1+1) * int((v/_min1)))