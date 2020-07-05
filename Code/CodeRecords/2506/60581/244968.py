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

if len(lst) == 0:
    print("0")
else:
    answer = [1]*len(lst)
    for i in range(1,len(lst)):
        theMax = 0
        for j in range(0,i):
            if lst[i]>lst[j]:
                theMax = max(theMax,answer[j])
            if theMax:
                answer[i] = theMax + 1

    print(theMax)

