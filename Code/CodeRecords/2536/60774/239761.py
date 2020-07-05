def getSec(item):
    return item[1]
ticLst = input()[1:-2].replace(' ','').split('],')
ticD = []
for tic in ticLst:
    dep = tic[2:5]
    des = tic[8:11]
    ticD.append([dep,des])
ticD.sort(key = getSec)
route = ['JFK']
start = 'JFK'
flag = True
while(len(ticD) != 0 and flag):
    flag = False
    for i in range(0,len(ticD)):    
        if(start == ticD[i][0]):        
            route.append(ticD[i][1])
            start = ticD[i][1]
            ticD.pop(i)
            flag = True
            break
print(route)