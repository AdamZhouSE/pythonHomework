list1 = eval(input())
list2=[]
list2.append('JFK')

while len(list1) != 0:
    From = list2[-1]
    To = 'XXX'
    for i in list1:
        if i[0]==From and i[1]<To:
            To=i[1]
    list2.append(To)
    list3=[]
    list3.append(From)
    list3.append(To)
    list1.remove(list3)
    
print(list2)    
    
    
