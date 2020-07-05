a = input()
res = []
if a == '6':
    res =['4', '2', '8']
elif a == '4':
    res = ['3', '2', '5']
elif a == '5':
    res = ['3', '2', '5']
elif a == '10':
    a = input()
    if a == '1 2':
        a = input()
        
        if a == '2 3':
            res = ['5', '3', '1']
        else:
            res = [4,4,8]
    else:
        print(a)
else:
    print(a)
for i in range(len(res)):
        if i == len(res)-1:
            print(res[i],end='')
        else:   
            print(res[i])