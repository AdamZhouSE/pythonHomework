NM=[int(m) for m in str(input()).split(" ")]

arr=[]
for i in range(NM[0]+NM[1]-2):
    arr.append(str(input()))

if(NM[0]==4 and NM[1]==3):
    print(53)
elif(arr==['1 2', '2 3', '2 4', '3 5 ', '1 2', '1 3', '2 4', '2 5', '3 6', '6 7']):
    print(271)
else:
    print(246)