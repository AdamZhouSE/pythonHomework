num = int(input())
namedict = {}
#pointlist = []
firstchampion = ''
maxpoint = 0
for i in range(num):
    str = input().split(' ')
    point = int(str[1])
    name = str[0]
    if not str[0] in namedict:
        namedict[name] = point
    else:
        point = namedict[name] + point
        namedict[name] = point 
    if point>maxpoint:
        firstchampion = name
        maxpoint = point
print(firstchampion)