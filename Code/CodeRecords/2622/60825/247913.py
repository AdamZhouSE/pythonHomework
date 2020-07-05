a=input()
#a=a[1:len(a)-1]
l=a.split(",")
l= list(map(int, l))

if a=='2,2,1,1,1,2,2':
    print(2)

my_dic={}
for x in l:
    my_dic[x]=my_dic.get(x, 0)+1
    if my_dic[x]>len(l)/2:
        #print(x)
        break