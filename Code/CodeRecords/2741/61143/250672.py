list_int = input()
lens = []
l_s = 1
temp = 0
for i in range(len(list_int)):
    temp = list_int[i]
    for j in range(i+1,len(list_int)):
        if list_int[j]>temp:
            temp = list_int[j]
            l_s +=1
        else:
            break
        lens.append(l_s)
        l_s = 1
lens.sort()
l = len(lens)
print(lens[l-1])