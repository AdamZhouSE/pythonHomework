cnt=int(input())
for i in range(0,cnt):
    list1=list(map(int,input().split(' ')))
    list2=list(map(int,input().split(' ')))
    list3 = list(map(int, input().split(' ')))
    for j in list3:
        list2.append(j)
    dict={}
    for j in list2:
        dict[j]=dict.get(j,0)+1
    print(len(dict))