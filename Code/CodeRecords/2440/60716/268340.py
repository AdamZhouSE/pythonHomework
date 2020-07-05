def insert(k:int):
#    print("insert:{}".format(k))
    if len(sortd)==0:
        sortd.append(k)
    else:
        for i in range(len(sortd)):
            if i == len(sortd)-1: 
                sortd.append(k)
                break
            if k>sortd[i] and k<=sortd[i+1]:
                sortd.insert(i+1,k)
                break
#    print(sortd)
lists = list(eval(input()))
#print(lists)
sortd = list()
while True:
    temp = lists.pop(0)
    insert(temp)
    if len(lists)==0: break
print(sortd)