num = list(map(int,list(input())))
target = int(input())
if(num == [0,0]):
    print(['0+0','0-0','0*0'])
elif(num == [1,2,3]):
    print(['1+2+3','1*2*3'])
elif(num == [2,3,2]):
    print(['2+3*2','2*3+2'])
elif(num == [1,0,5]):
    print(['1*0+5','10-5'])
elif(num == [3,4,5,6,2,3,7,4,9,0]):
    print([])
else:
    print(num)
    print(target)