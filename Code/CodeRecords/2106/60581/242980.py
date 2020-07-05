str = input()

lst = []
i = 0
lst = []
while i < len(str):
    number = ''
    judge = False
    if str[i]>='0' and str[i]<='9':
        judge = True
        number += str[i]
    if str[i]=='(':
        lst.append('(')
    elif str[i]==')':
        lst.append(')')
    elif str[i]=='+':
        lst.append('+')
    elif str[i]=='-':
        lst.append('-')
    while judge:
        if i+1 == len(str):
            lst.append(int(number))
            break
        if str[i+1] >= '0' and str[i+1] <= '9':
            i += 1
            number += str[i]
        else:
            judge = False
            lst.append(int(number))
    i += 1

forehead = 0
after = 0
judgeAfter = False

while lst.count(')') != 0 :
    steps = []
    for i in range(0,len(lst)):
        if lst[i]==')':
            after = i
            break
    for i in range(0,after):
        if lst[after-i-1]=='(':
            forehead = after - i - 1
            break
    number = lst[forehead+1]
    count = forehead + 2
    while count < after:
        if lst[count]=='+':
            number += lst[count+1]
        elif lst[count]=='-':
            number -= lst[count+1]
        count += 2
    for i in range(0,forehead):
        steps.append(lst[i])
    steps.append(number)
    for i in range(after+1,len(lst)):
        steps.append(lst[i])
    lst = steps

if len(lst)!= 1:
    number = lst[0]
    count = 1
    while count < len(lst):
        if lst[count]=='+':
            number += lst[count+1]
        elif lst[count]=='-':
            number -= lst[count+1]
        count += 2

print(number)