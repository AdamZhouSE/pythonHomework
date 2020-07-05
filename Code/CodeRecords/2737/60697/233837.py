abc=input();
a=len(abc)
array=abc[1:a-1].split(',')
res=[]
dict={}
len=len(array)
for i in range(len):
    dict[array[i]]=0
for i in range(len):
    dict[array[i]]=dict[array[i]]+1
for i in dict.keys():
    if dict.get(i)>len/3:
        res.append(int(i))
print(res)