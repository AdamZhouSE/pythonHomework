s = input().split(",")
lists = list(s)
#print(lists)
arr1 = lists[0]
arr2 = lists[1]
#print(arr1)
#print(arr2)
lists1 = list(arr1)
lists2 = list(arr2)
#print(lists1)
#print(lists2)

number = ['0','1','2','3','4','5','6','7','8','9']

def func(lists):
    res = ""
    flag = False
    for i in range(len(lists)):
        if lists[i] == '-':
            flag = True

    for i in range(len(lists)):
        temp = lists[len(lists)-1-i]
        for j in range(number.__len__()):
            if number[j] == temp:
                res = temp + res
    if flag:
        res = "-" + res

    return res

dividend = func(lists1)
divisor = func(lists2)
#print(dividend)
#print(divisor)
dividend = int(dividend)
divisor = int(divisor)
ans = int(dividend/divisor)
print(ans)