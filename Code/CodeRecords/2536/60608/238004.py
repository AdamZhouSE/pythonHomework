import re
def func6(nums):
    place1 = "JFK"
    tem = "JKF"
    n = len(nums)
    counter = 0
    result.append(place1)
    array3 = []

    while counter < n:
        flag = 0
        for index, item in enumerate(nums):
            if item[0] == place1 and array3.count(index) == 0:
                if flag == 0:
                    flag = 1
                    tem = item[1]
                else:
                    if tem > item[1]:
                        tem = item[1]
        array3.append(array2.index([place1, tem]))
        place1 = tem
        result.append(place1)
        counter += 1


result = []
string = input()
pattern = r'\w{3}'
array1 = re.findall(pattern, string)
array2 = []
n1 = len(array1)
counter1 = 0
while counter1 < n1:
    array2.append(array1[counter1:counter1 + 2])
    counter1 += 2
func6(array2)
print(result)
