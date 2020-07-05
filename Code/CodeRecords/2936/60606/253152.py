test_num = int(input())
result = []
for i in range(test_num):
    result.append(input())
for i in range(len(result)):
        result[i] = result[i].replace('A', '2')
        result[i] = result[i].replace('B', '2')
        result[i] = result[i].replace('C', '2')
        result[i] = result[i].replace('D', '3')
        result[i] = result[i].replace('E', '3')
        result[i] = result[i].replace('F', '3')
        result[i] = result[i].replace('G', '4')
        result[i] = result[i].replace('H', '4')
        result[i] = result[i].replace('I', '4')
        result[i] = result[i].replace('J', '5')
        result[i] = result[i].replace('K', '5')
        result[i] = result[i].replace('L', '5')
        result[i] = result[i].replace('M', '6')
        result[i] = result[i].replace('N', '6')
        result[i] = result[i].replace('O', '6')
        result[i] = result[i].replace('P', '7')
        result[i] = result[i].replace('R', '7')
        result[i] = result[i].replace('S', '7')
        result[i] = result[i].replace('T', '8')
        result[i] = result[i].replace('U', '8')
        result[i] = result[i].replace('V', '8')
        result[i] = result[i].replace('W', '9')
        result[i] = result[i].replace('X', '9')
        result[i] = result[i].replace('Y', '9')

        result[i] = result[i].replace('-','')

set1 = set()
num = 0
sentinel = 0
for i in range(test_num):
    set1.add(result[i])
    if len(set1) == num:
        print(result[i][0:3],end="-")
        print(result[i][3:],end=" ")
        print(result.count(result[i]))
        sentinel = 1
        break
    else:
        num += 1
if sentinel == 0:
    print("No duplicates.",end="")



