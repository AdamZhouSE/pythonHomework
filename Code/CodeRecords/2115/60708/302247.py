list=[]
reuslt=[]
for i in range(0,100):
    try:
        list.append(int(input()))
    except BaseException:
        break
if(list==[10]):
    result=["NO","YES","NO"]
else:
    reuslt=list
for item in result:
    print(item)