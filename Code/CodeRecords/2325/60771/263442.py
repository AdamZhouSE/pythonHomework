#02
num = list(eval(input()))
# str = input().replace("[","")
# str = str.replace("]","")
# ori = str.split(",")
# num = [int(item) for item in ori]
num.sort()
numbers = []
index = 0
if len(num) == 1:
    print(False)
    exit(0)
while index < len(num)-1:
    temp = 0
    for i in range(index, len(num)):
        tar = num[i]
        for j in range(i + 1, len(num)):
            if tar == num[j]:
                temp = j
                continue
            else:
                temp = j
                break
        break
    if temp == len(num)-1:
        numbers.append(temp - index +1)
    else:
        numbers.append(temp - index)
    index = temp
flag = True
numbers.sort()
item = numbers[0]
for i in range(1,len(numbers)):
    # print("item: ",item)
    # print("number: ",numbers[i])
    if numbers[i] % item != 0:
        flag = False
        break
print(flag)
