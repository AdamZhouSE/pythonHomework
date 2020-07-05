str1=str(input())[1:-1].split(",")
zero=[]
one=[]
two=[]
for i in str1:
    if i=="0":
        zero.append(int(i))
    elif i=="1":
        one.append(int(i))
    else:
        two.append(int(i))
zero.extend(one)
zero.extend(two)
print (zero)