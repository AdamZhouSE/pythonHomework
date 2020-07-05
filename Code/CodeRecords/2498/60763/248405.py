A = eval(input())
a_list = [0]*len(A)
countQ = 1
countO = 0
for i in A:
    if i % 2 == 0:
        a_list[countO] = i
        countO +=2
    else:
        a_list[countQ] = i
        countQ += 2
print(a_list)