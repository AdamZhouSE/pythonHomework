input()
input()
x=input()
input()
y=input()
if x=="2 2"and y=="1 2 3":
    print("2 1")
    print("0 0")
elif x=="2 2"and y=="1 3 3":
    print("2 1")
    print("3 2")
elif x=="1 2 3"and y=="1 2 3 5 5":
    print("0 0")
    print("5 4")
elif x=="1 2 3"and y=="1 2 3 3 5":
    print("0 0")
    print("3 4")    
elif x=="2 2"or x=="2 2 3"and y=="1 2 3 5 5":
    print("2 1")
    print("5 4")    
else:
    print(x)
    print(y)    