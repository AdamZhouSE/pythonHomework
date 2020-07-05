list1 = [int(i) for i in list1]
k = int(input()) - 1
list2 = []
for i in range(len(list1) - 1):
    for j in range(i + 1, len(list1)):
        if list1[i] < list1[j]:
            list2.append(Fraction(list1[i], list1[j]))
list2.sort()
res = []
res.append(list2[k].numerator)
res.append(list2[k].denominator)
print(res)