def judge(input_string):
    arr = []
    telephone = ""
    arr = input_string.split("-")
    for j in range(len(arr)):
        telephone += arr[j]
    return telephone


def convert(input_str):
    input_str_l = list(input_str)
    result_Tele = 0
    for m in range(0, len(input_str)):
        if 'A' <= input_str_l[m] < 'Q':
            input_str_l[m] = int((ord(input_str_l[m]) - ord('A')) / 3 + 2)
        elif 'Q' < input_str_l[m] <= 'Z':
            input_str_l[m] = int((ord(input_str_l[m]) - ord('A') - 1) / 3 + 2)
        else:
            input_str_l[m] = int(input_str_l[m])
    for n in range(0, len(input_str_l)):
        result_Tele *= 10
        result_Tele += input_str_l[n]
    return result_Tele


num = int(input())
inputString = []
result = []
maximum = 1
final_Telephone = 0
for i in range(0, num):
    inputString.append(judge(input()))
for k in range(0, len(inputString)):
    result.append(convert(inputString[k]))
for x in range(0, len(result)):
    if result.count(result[x]) > maximum:
        final_Telephone = result[x]
        maximum = result.count(result[x])
if maximum == 1:
    print("No duplicates.", end="")
else:
    print(int(final_Telephone / 10000), end="")
    print("-", end="")
    print(final_Telephone % 10000, end=" ")
    print(maximum)
