inp = input()
length = len(inp)
list1 = []
i = 0
while i <= length - 1:
    temp = []
    while i <= length - 1:
        if inp[i].isdigit():
            temp.append(int(inp[i]))
        elif inp[i] == ']':
            break;
        i += 1
    i += 1
    if (len(temp) != 0):
        list1.append(temp)
restaurants=list1
veganFriendly=int(input())
maxPrice=int(input())
maxDistance=int(input())
dic = {}
for restaurant in restaurants:
    if veganFriendly == 0:
        if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance:
                dic[restaurant[0]] = restaurant[1]
    else:
        if restaurant[3] <= maxPrice and restaurant[4] <= maxDistance and restaurant[2] == 1:
                dic[restaurant[0]] = restaurant[1]
res = []
dic = sorted(dic.items(), key = lambda x:[x[1],x[0]],reverse=True)
for i in dic:
    res.append(i[0])
print(res)