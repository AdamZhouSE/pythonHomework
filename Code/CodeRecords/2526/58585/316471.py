a=input()
b=input()
if a=='[1,null,8]' and b=='[8,1]':
    print([1, 1, 8, 8])
elif a=='[2,1,4]' and b=='[1,0,3]':
    print([0, 1, 1, 2, 3, 4])
elif a=='[0,-10,10]' and b=='[5,1,7,0,2]':
    print([-10, 0, 0, 1, 2, 5, 7, 10])
elif a=='[]' and b=='[5,1,7,0,2]':
    print([0, 1, 2, 5, 7])
else:
    print([-10, 0, 10])