ff = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
ff = [list(i) for i in ff]
s = list(input())
ans = list()
while s:
    i = s[0]
    for j in ff:
        if i in j:
            flag = True
            for k in j:
                if k not in s:
                    flag = False
                    break
            if flag:
                for k in j:
                    s.remove(k)
                ans.append(ff.index(j))
            break
ans.sort()
k = ''
for i in ans:
    k += str(i)
print(k)

