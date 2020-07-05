def select_restaurants(arr, vegan_frendly, max_price, max_distance):
    selected_list = []
    for i in range(len(arr)):
        if arr[i][2] >= vegan_frendly and arr[i][3] <= max_price and arr[i][4] <= max_distance:
            index = 0
            if len(selected_list) == 0:
                selected_list.append((arr[i][0], arr[i][1]))
            else:
                while arr[i][1] <= selected_list[index][1]:
                    if arr[i][1] == selected_list[index][1]:
                        if arr[i][0] < selected_list[index][0]:
                            index += 1
                        else:
                            break
                    else:
                        index += 1
                    if index == len(selected_list):
                        break
                selected_list.insert(index, (arr[i][0], arr[i][1]))
    final_list = []
    for i in range(len(selected_list)):
        final_list.append(selected_list[i][0])
    return final_list


raw_res = input()[2:-2].split('],[')
restaurants = []
for i in range(len(raw_res)):
    restaurants.append(raw_res[i].split(','))
    for j in range(5):
        restaurants[i][j] = int(restaurants[i][j])
print(select_restaurants(restaurants, int(input()), int(input()), int(input())))