cnt=int(input())
for i in range(0,cnt):
    k=input()
    list1=[str(e) for e in input().split(' ')]
    dict={}
    for temp in list1:
        list2=list(temp)
        list2.sort()
        dict["".join(list2)]=dict.get("".join(list2),0)+1
    list3=[]
    for j in dict.values():
        list3.append(j)
    list3.sort()
    for j in range(0,len(list3)):
        if j!=len(list3)-1:
            print(list3[j],end=' ')
        else:
            print(list3[j])