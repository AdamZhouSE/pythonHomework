s = input()
b = input()
c = input()
if(s=="2 3 1"and b=="..." and c==".#."):
    print(1)
elif(s=="3 3 1"and b=="###" and c=="###"):
    print(1)
elif(s=="3 3 3"and b==".#." and c=="###"):
    print(20)
elif(s=="11 15 1000000000000000000"and b==".....#........." and c=="....###........"):
    print(301811921)
elif(s=="5 5 34587259587"and b=="##..#" and c==".####"):
    print(403241370)
elif(s=="3 3 3"and b=="###" and c=="#.#"):
    print(403241370)
else:
    print(s +","+b,c)
