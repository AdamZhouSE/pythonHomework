k_list=list (map(str,input().replace('[[','').replace(']]','').split('],[')))
                       #[[1,4,5],[1,3,4],[2,6]]
list=[]
for i in k_list:

    i=[int(item) for item in i.split(',')]
    i.sort()
   
    list.append(i)


count=1
while count<len(list):
    for i in list[count]:
        list[0].append(i)
    count=count+1

list[0].sort()

print(list[0])