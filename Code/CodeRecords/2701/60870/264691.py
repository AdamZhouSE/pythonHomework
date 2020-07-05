def winOrLose(array):
    if (array[0] == 1 and array[1] == 1 and array[2] == 1) or (array[3] == 1 and array[4] == 1 and array[5] == 1) or (
            array[6] == 1 and array[7] == 1 and array[8] == 1) or (
            array[0] == 1 and array[4] == 1 and array[8] == 1) or (array[2] == 1 and array[4] == 1 and array[6] == 1):
        return 'B'
    elif (array[0] == 0 and array[1] == 0 and array[2] == 0) or (array[3] == 0 and array[4] == 0 and array[5] == 0) or (
            array[6] == 0 and array[7] == 0 and array[8] == 0) or (
            array[0] == 0 and array[4] == 0 and array[8] == 0) or (array[2] == 0 and array[4] == 0 and array[6] == 0):
        return 'A'
    elif -1 not in array:
        return 'Draw'
    else:
        return 'Pending'


str_chess = input()
str_valid = ''
for ch in str_chess:
    if '9' >= ch >= '0':
        str_valid = str_valid + ch
dict_chess = {'00': 0, '01': 1, '02': 2, '10': 3, '11': 4, '12': 5, '20': 6, '21': 7, '22': 8}
array_judge = []
for i in range(9):
    array_judge.append(-1)
for i in range(0, len(str_valid), 2):
    index = dict_chess[str_valid[i] + str_valid[i + 1]]
    if i % 4 == 0:
        array_judge[index] = 0
    else:
        array_judge[index] = 1
print(winOrLose(array_judge))