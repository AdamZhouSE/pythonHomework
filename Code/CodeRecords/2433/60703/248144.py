list1 = eval(input());
if(len(list1)<=1):
    print(list1)
else:
    res = [];
    list1.sort(key = lambda x:x[0]);

    for innerList in list1:
       # print(innerList);
        if not res or res[-1][1]<innerList[0]:
#            print(res[-1]);
            res.append(innerList);
        else:
            res[-1][1]= max(res[-1][1],innerList[1]);

    print(res);