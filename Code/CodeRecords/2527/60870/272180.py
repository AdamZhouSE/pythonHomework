str_input = input()
str_input = str_input.replace('[', '')
str_input = str_input.replace(']', '')
str_valid = str_input.split(',')
str_valid = [int(x) for x in str_valid]
restaurant_list = []
for i in range(0, len(str_valid), 5):
    restaurant = []
    for j in range(i, i + 5):
        restaurant.append(str_valid[j])
    restaurant_list.append(restaurant)
ifVeg = int(input())
maxPrice = int(input())
maxDistance = int(input())
restaurant_dict = {}
for ch in restaurant_list:
    if ifVeg == 0:
        if ch[3] <= maxPrice and ch[4] <= maxDistance:
            restaurant_dict[ch[0]] = ch[1]
    else:
        if ch[2] == 1 and ch[3] <= maxPrice and ch[4] <= maxDistance:
            restaurant_dict[ch[0]] = ch[1]
restaurant_dict = sorted(restaurant_dict.items(), key = lambda x : x[1], reverse = True)
res = []
for i in range(len(restaurant_dict) - 1):
    for j in range(i + 1, len(restaurant_dict)):
        if restaurant_dict[i][1] == restaurant_dict[j][1] and restaurant_dict[i][0] < restaurant_dict[j][0]:
            temp = restaurant_dict[i]
            restaurant_dict[i] = restaurant_dict[j]
            restaurant_dict[j] = temp
for ch in restaurant_dict:
    res.append(ch[0])
for i in range(len(res)):
    if i == 0: 
        print('[' + str(res[i]) + ',', end = ' ')
    elif i == len(res) - 1:
        print(str(res[i]) + ']')
    else:
        print(str(res[i]) + ',', end = ' ')