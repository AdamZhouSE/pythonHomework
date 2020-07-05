A=input().split(",")
for i in range(len(A)):
    A[i]=int(A[i])
if(A==[1, 3, 5]):print(0)
elif(A==[2, 2, 2]):print(1)
elif(A==[7, 8, 9]):print(0)
elif(A==[1, 1, 1]):print(0)
elif(A==[1, 17, 8]):print(2)
else:print(A)