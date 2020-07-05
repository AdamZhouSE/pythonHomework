def res_filter(ls: list, veg: int, price: int, distance: int) -> list:
    res = []
    for i in ls:
        if veg == 1:
            if i[2] == veg and i[3] <= price and i[4] <= distance:
                res.append(i)
        else:
            if i[3] <= price and i[4] <= distance:
                res.append(i)
    final = sorted(res, key=lambda x: [-x[1], -x[0]])
    des = [i[0] for i in final]
    return des


res_ls = eval(input())
veg_fil = int(input())
price_fil = int(input())
dis_fil = int(input())
print(res_filter(res_ls, veg_fil, price_fil, dis_fil))