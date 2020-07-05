alp = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
all = input()[2:-2].split("\", \"")
w = input()
min = 1000
for i in all:
    temp = alp.index(i)-alp.index(w)
    if temp<=0:
        temp = temp+26
    if temp<min:
        min = temp
for i in all:
    temp = alp.index(i)-alp.index(w)
    if temp<0:
        temp = temp+26
    if temp==min:
        print(i)
        break