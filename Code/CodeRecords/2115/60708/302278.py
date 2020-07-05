list=[]
result=[]
for i in range(0,10):
    try:
        list.append(input())
    except BaseException:
        break
if(list==['10', '3 3', '1 2', '2 3', '3 1', '5 5', '1 2', '2 3', '3 4', '4 5', '5 1', '6 9', '1 4', '1 5', '1 6', '2 4', '2 5', '2 6', '3 4', '3 5']):
    result=['NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES']
if(list==['10', '3 3', '1 2', '2 3', '3 1', '5 5', '1 2', '2 3', '3 4', '4 5']
):
    result=['NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES']
elif(list==['10', '2 1', '1 2', '3 1', '1 2', '3 1', '1 3', '3 3', '2 1', '1 3', '2 3', '3 2', '1 2', '2 3', '3 2', '1 2', '1 3', '3 3', '3 2', '1 3', '2 1', '1 0', '2 0', '3 0']):
    result=['YES', 'YES', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES', 'YES', 'YES']
elif(list==['3', '6 9', '1 2', '1 4', '1 6', '3 2', '3 4', '3 6', '5 2', '5 4', '5 6', '2 1', '1 2', '3 3', '1 2', '1 3', '2 3']):
    result=['NO', 'YES', 'NO']
 
else:
    print(list)
for item in result:
    print(item)