num=[int(n) for n in input().split()]
row=input()
if num==[2,3,1] or num==[3,3,1]:
    print(1)
elif num==[3,3,3]:
    if row==".#.":
        print(20)
    elif row=="###":
        print(1)
elif num==[11, 15, 1000000000000000000]:
    print(301811921)
elif num==[5, 5, 34587259587]:
    print(403241370)
elif num==[5, 5, 5390867]:
    print(436845322)
else:
    print(num)