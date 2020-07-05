a = eval(input())
odd = [x for x in a if x % 2 == 1]
even = [x for x in a if x % 2 == 0]
r = []
for i in range(round(len(a) / 2)):
    r.append(even[i])
    r.append(odd[i])
print(r)