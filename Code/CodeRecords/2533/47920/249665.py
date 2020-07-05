import sys
temp1 = []
temp2 = []
inp =eval(input())
for i in inp:
    if i%2 == 0:
        temp1.append(i)
    else:
        temp2.append(i)
print(temp1+temp2)




