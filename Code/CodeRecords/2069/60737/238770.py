def my_mul(a, b):
    if (a == '0') or (b == '0'):
        return '0'
    lista = list(a)
    lena = len(lista)
    listb = list(b)
    lenb = len(listb)
    multi = [0] * (lena + lenb)
    for i in range(lena):
        for j in range(lenb):
            x = int(lista[i]) * int(listb[j])
            if x > 9:
                multi[i+j+1] = x%10+multi[i+j+1]
                multi[i+j] = int(x/10)+multi[i+j]
            else:
                multi[i+j+1] = x+multi[i+j+1]
    for i in range(1, 1+len(multi)):
        if multi[len(multi)-i]>9:
            multi[len(multi)-i-1] += int(multi[len(multi)-i]/10)
            multi[len(multi)-i] = multi[len(multi)-i]%10
    ans = []
    for i in range(len(multi)):
        ans.append(str(multi[i]))
    if ans[0] == '0':
        ans.remove('0')
    return ''.join(ans)


if __name__ == "__main__":
    a = input()
    b = input()
    print(my_mul(a, b))
