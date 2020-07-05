a=input()
l=a.split(",")
l= list(map(int, l))

my_dic={}
for x in l:
    my_dic[x]=my_dic.get(x, 0)+1
    if my_dic[x]>len(l)/2:
        print(x)
        break