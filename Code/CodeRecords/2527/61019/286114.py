info = eval(input())
veg = eval(input())
mprice = eval(input())
mdis = eval(input())

info = [i for i in info if (not veg or i[2]) and mprice >= i[3] and mdis >= i[4]]
info.sort(key=lambda x: (x[1], x[0]),reverse=True)
index = [i[0] for i in info]
print(index)
