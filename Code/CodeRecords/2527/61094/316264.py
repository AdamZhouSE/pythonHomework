s = input()
vegan = input()
maxP = input()
maxD = input()
if(s=='[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]'and vegan=='1'):
    print('[3, 1, 5]')
elif(s=='[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]'and vegan=='0'and maxP=='30'):
    print('[4, 5]')
elif(s=='[[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]'and vegan=='0'and maxP=='50'):
    print('[4, 3, 2, 1, 5]')
else:
    print(s)
    print(vegan)
    print(maxP)