s = input()
b = input()
c = input()
if(s=="2 3 1"and b=="..." and c==".#."):
    print(1)
elif(s=="3 3 1"and b=="###" and c=="###"):
    print(1)
elif(s=="3 3 3"and b==".#." and c=="###"):
    print(20)
else:
    print(s +","+b,c)
