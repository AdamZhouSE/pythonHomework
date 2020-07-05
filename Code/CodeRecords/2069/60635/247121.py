src1=input()
src2=input()


def mutiply(string,num):
    def carry_solver(array):
        i=0
        while i<len(array):
            carrier = array[i] // 10
            if carrier > 0:
                if i == len(array)-1:
                    array.append(carrier)
                else :
                    array[i+1] += carrier
            array[i]=array[i]%10
            i += 1
    res=[int(x) for x in string][::-1]
    for i,a in enumerate(res):
        res[i]=a*num
    carry_solver(res)
    res=[str(x) for x in res]
    return int(''.join(res[::-1]))


if src1 == '0' or src2=='0':
    print('0')
step = 1
ans = 0
for a in list(src2)[::-1]:
    ans += step*mutiply(src1,int(a))
    step *= 10
print(ans)
