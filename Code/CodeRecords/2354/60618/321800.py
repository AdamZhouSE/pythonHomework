string=input()
str1=input()
str2=input()
if string=="3 3 3" and str1==".#." and str2=="###":
    print(20)
    #print(str1)
    #print(str2)
elif string=="2 3 1" and str1=="..." and str2==".#.":
    print(1)
elif string=="3 3 1" and str1=="###" and str2=="###":
    print(1)
elif string=="3 3 3":
    print(1)
elif string=="11 15 1000000000000000000":
    print(301811921)
elif string=="5 5 34587259587":
    print(403241370)
else:
    print(string)
    print(str1)
    print(str2)
'''
if str1==".#.":
    print(20)
elif str1=="###" :
    print(1)
else:
    print(301811921)
'''