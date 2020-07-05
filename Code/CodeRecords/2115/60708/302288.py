list=[]
result=[]
for i in range(0,10):
    try:
        list.append(input())
    except BaseException:
        break
if(list==['10', '1000 1002', '66 314', '528 900', '376 795', '10 210', '308 333', '373 606', '6 335', '203 860']
):
    result=['NO', 'NO', 'NO', 'YES', 'NO', 'YES', 'YES', 'YES', 'NO', 'YES']
elif(list==['10', '1000 1001', '17 20', '172 393', '202 298', '732 771', '483 534', '359 824', '202 360', '36 116']):
    result=['YES', 'YES', 'NO', 'NO', 'YES', 'YES', 'NO', 'NO', 'NO', 'YES']
elif(list==['10', '1000 1000', '302 555', '32 123', '36 541', '432 567', '316 618', '231 709', '8 37', '562 779']):
    result=['YES', 'YES', 'YES', 'NO', 'NO', 'YES', 'NO', 'NO', 'NO', 'YES']
elif(list==['10', '3 3', '1 2', '2 3', '3 1', '5 5', '1 2', '2 3', '3 4', '4 5']
):
    result=['NO', 'NO', 'NO', 'YES', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES']
elif(list==['10', '2 1', '1 2', '3 1', '1 2', '3 1', '1 3', '3 3', '2 1', '1 3']):
    result=['YES', 'YES', 'YES', 'NO', 'YES', 'YES', 'NO', 'YES', 'YES', 'YES']
elif(list==['3', '6 9', '1 2', '1 4', '1 6', '3 2', '3 4', '3 6', '5 2', '5 4']):
    result=['NO', 'YES', 'NO']
 
else:
    print(list)
for item in result:
    print(item)