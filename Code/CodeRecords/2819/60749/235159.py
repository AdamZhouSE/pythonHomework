
total_num = int(input())
m = []
m.append(list(map(int, input().split(" "))))
input = m[0]
store_number = [0, 0, 0, 0]
for x in range(0, total_num, 1):
    if input[x] == 1:
        store_number[0] = store_number[0] + 1
    if input[x] == 2:
        store_number[1] = store_number[1] + 1
    if input[x] == 3:
        store_number[2] = store_number[2] + 1
    if input[x] == 4:
        store_number[3] = store_number[3] + 1
result = store_number[3]
if store_number[2] >= store_number[0]:
    result = result + store_number[2]
    result = (store_number[1] + 1) // 2+result
    print(result)
else:
    result = result + store_number[2]
    store_number[0] = store_number[0] - store_number[2]
    if store_number[1] % 2 == 1:
        result = (store_number[1] + 1) // 2 + result
        if store_number[0] > 2:
            store_number[0] = store_number[0] - 2
            if store_number[0] % 4 > 0:
                result = result + 1 + store_number[0] // 4
                print(result)
            else:
                result = result + store_number[0] // 4
                print(result)
    else:
        result=store_number[1]// 2 + result
        result=store_number[0]//4+result
        if store_number[0]%4:
            result=result+1
            print(result)
        else:
            print(result)

