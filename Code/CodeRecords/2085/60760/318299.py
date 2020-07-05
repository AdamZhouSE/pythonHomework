def func(maps:list):

    return sum(maps)
i=input()
maps=[]
while len(i)>0:  #第一个数是开始顶点，第二个数是结束顶点，第三位是路长
    maps.append(list(map(int,i.split(' '))))
    i=input()
res=func(maps)
print(res,end="")