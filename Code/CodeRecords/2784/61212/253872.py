temp = list(input().split(" "))
numOfCan = int(temp[0])
numOfCity = int(temp[1])
city = []

for i in range(0, numOfCan):
    city.append(0)

for i in range(0, numOfCity):
    lists = list(input().split(" "))
    listInCity = []
    for j in range(0, numOfCan):
        listInCity.append(int(lists[j]))
    index = listInCity.index(max(listInCity))
    city[index] = city[index] + 1

print(city.index(max(city))+1)
