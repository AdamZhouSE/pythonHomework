n=int(input())
info=input().split(' ')
a=[int(y) for y in info]
dict={}
for j in a:
    if j not in dict.keys():
        dict[j]=1
    else:
        dict[j]=dict[j]+1
if 0 in dict.keys():
    print(len(dict)-1)
else:
    print(len(dict))

        