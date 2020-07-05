def decimal_T(string:str):
    lista = list(string)
    if lista[0]!=1:
        return False
    else:
        c = lista[0]
        for t in range(lista):
            if t%2==0 and lista[t]=='1':
                continue
            elif t%2==1 and lista[t]=='0':
                continue
            else:
                return False
        return True
def binary_T(number:int):
    index = 0
    temp10 = 0
    temp01 = 0
    while True:
        if temp10 == number or temp01 == number:
            return True
        elif temp10 >number and temp01 > number:
            return False
        else:
            if index%2==0:
                temp10 += (2**index)
                index += 1
            else:
                temp01 += (2**index)
                index += 1
ucnum = int(input())
ans = list()
for i in range(ucnum):
    strs = input()
    num = int(strs)
    anslist = list()
    for j in range(1,num+1):
        check_decimal = decimal_T(str(j))
        check_binary   = binary_T(j)
        if check_binary or check_decimal:
            anslist.append(j)
    ans.append(anslist)  
for i in ans:
    for k in range(len(i)):
        print(i[k],end=' ') if k!=len(i)-1 else print(i[k])
