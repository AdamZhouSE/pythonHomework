a=input()
#a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))

my_dic={}
for x in l:
    my_dic[x]=my_dic.get(x, 0)+1
    if my_dic[x]>=en(l)/2:
        print(x)
        break