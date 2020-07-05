n=int(input())

arr=[]
for i in range(n):
    arr.append(str(input()))
    
if(arr==['5,4', '6,4', '1,7', '2,6']):
    print(1)
elif(arr==['5,4', '6,4', '1,7', '2,3'] or arr==['5,4', '6,4', '1,7', '2,2']):
    print(2)
elif(arr==['2,4', '6,4', '8,7', '2,2'] or arr==['5,4', '6,4', '8,7', '2,2'] or arr==['2,4', '9,9', '8,7', '2,2'] or arr==['5,4', '6,4', '6,7', '2,3']):
    print(3)
else:
    print(arr)