num = int(input())
str1 = input().split(' ')
lists = [int(i) for i in str1]
adda = 0
for i in lists:
    adda+=i
if adda%3!=0:
    print(0)
else:
    average = adda//3
    index=0
    lists.insert(0,0)
    lists.append(0)
    first = 0
    for i in range(len(lists)):
        first+=lists[i]
        if first==average and i!=len(lists)-1 and i!=0:
            second = 0
            for j in range(i+1,len(lists)):
                second+=lists[j]
                if second==average and j!=len(lists)-1 and j!=0:
                    index+=1
#    if(index==6):
#        print(lists)
    print(index)