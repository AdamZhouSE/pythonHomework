str = input()
i = 0
lst = []
while i < len(str):
    number = ''
    judge = False
    if str[i]=='-' or (str[i]>='0' and str[i]<='9'):
        judge = True
        number += str[i]
    while judge:
        if i + 1 == len(str):
            lst.append(int(number))
            break
        if str[i + 1] >= '0' and str[i + 1] <= '9':
            i += 1
            number += str[i]
        else:
            judge = False
            lst.append(int(number))
    i += 1
lst.sort()
maxNumber = 1
for i in range(len(lst)-1):
    number = 1
    for j in range(i+1,len(lst)):
        if lst[j] == lst[i] + j - i :
            number += 1
        else:
            break
    if maxNumber < number:
        maxNumber = number

print(maxNumber)