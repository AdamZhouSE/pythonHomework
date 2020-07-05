str = input()
str = str[1:len(str) - 1]
A = str.split(",")
even_num = []
odd_num = []
for i in A:
    if int(i) % 2 == 0:
        even_num.append(int(i))
    else:
        odd_num.append(int(i))
A = even_num + odd_num
#print(even_num)
#print(odd_num)
print(A)
