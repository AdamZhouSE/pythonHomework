list=[]
reuslt=[]
for i in range(0,100):
    try:
        list.append(int(input()))
    except BaseException:
        break
print(list)
result=["NO","YES","NO"]
for item in result:
    print(item)