str = input()
dict = {}
for i in str:
    dict[i] = dict.get(i,0) + 1
dict = sorted(dict.items(),reverse=True,key=lambda kv:(kv[1],kv[0]))
out = ''
for j in dict:
    out = out + j[0]*j[1]
print(out)