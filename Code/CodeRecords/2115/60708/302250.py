list=[]
result=[]
for i in range(0,100):
    try:
        list.append(input())
    except BaseException:
        break
if(list==[10]):
    result=["NO","YES","NO"]
else:
    print(list)
for item in result:
    print(item)