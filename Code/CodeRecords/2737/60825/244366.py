aaa=input()
aaa=aaa[1:len(aaa)-1]
l=aaa.split(",")
l= list(map(int, l))

N=len(l)
res=[]
my_dic={}

for x in l:
    my_dic[x]=my_dic.get(x, 0)+1
    
for x in my_dic:
    if my_dic[x]>N/3:
        res.append(x)

print(res)