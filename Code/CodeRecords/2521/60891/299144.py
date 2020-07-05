a = eval(input())
a_set = set(a)
a_count = []
set_len = len(a_set)
for i in range(set_len):
    a_count.append([])
for i in range(set_len):
    x = a_set.pop()
    a_count[i].append(x)
    a_count[i].append(a.count(x))
a_count.sort(key=lambda t: t[1])
a = []
for i in range(set_len):
    for j in range(a_count[i][1]):
        a.append(a_count[i][0])
ans_l = [a[0]]
form_x = a[0]
a.remove(form_x)
while len(a) > 0:
    for i in range(len(a)):
        if a[i] != form_x:
            form_x = a[i]
            break
    ans_l.append(form_x)
    a.remove(form_x)
print(ans_l)
