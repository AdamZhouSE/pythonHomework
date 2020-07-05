n = int(input())
d = input()
list_s = d.split()
new_list_s = []
for m in list_s:
    new_list_s.append(int(m))
list_x = list(set(new_list_s))
list_x.sort()
if len(list_x) == 1:
    D = 0
elif len(list_x) == 2:
    D = list_x[1]-list_x[0]
    if D%2 == 0:
        D = int(D/2)
elif len(list_x) == 3:
    if list_x[2] + list_x[0] == 2*list_x[1]:
        D = list_x[1]-list_x[0]
    else:
        D = -1
else:
    D = -1
print(D)
