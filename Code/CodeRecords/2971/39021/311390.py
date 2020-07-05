s = input()
print(s)
dict = {}
for i in range(len(s)):
    dict[i+1]=s[i]
list = sorted(dict.items(),key=lambda x:(x[1],-x[0]))
print(list)
res = [str(i[0]) for i in list]
a = ' '.join(res)
print(a)