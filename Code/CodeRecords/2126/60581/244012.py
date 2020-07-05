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

max = []
for i in range(0,len(lst)-1):
    output = []
    output.append(lst[i])
    for j in range(i+1,len(lst)):
        judge = True
        for h in range(0,len(output)):
            if lst[j]%output[h]!=0 and output[h]%lst[j]!=0:
                judge = False
        if judge:
           output.append(lst[j])
    if len(output) > len(max):
        max = output

print(max)
