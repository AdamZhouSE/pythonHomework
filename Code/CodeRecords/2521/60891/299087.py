a = eval(input())
a.sort(reverse=True)
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
