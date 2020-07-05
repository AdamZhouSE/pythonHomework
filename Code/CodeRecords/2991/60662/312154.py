s1 = list(str(input()))
s1.reverse()
new = []
for i in s1:
    if i != ' ':
        new.append(i)
print(''.join(new),end='')