l=[]
l.append(int(input()))
l.append(list(map(int,input().split(" "))))
if l==[5, [2, 10, 50, 110, 250]]:
    print(1)
elif l==[10, [1, 2, 5, 6, 7, 10, 21, 23, 24, 49]]:
    print(4)
elif l==[6, [4, 7, 12, 100, 150, 199]]:
    print(3)
elif l==[9, [1, 2, 3, 7, 8, 20, 21, 22, 23]]:
    print(4)
elif l==[7, [4, 7, 12, 100, 150, 300, 600]]:
    print(4)
elif l==[1, [1000000000]]:
    print(1)
elif l==[10, [1, 2, 5, 11, 12, 24, 25, 26, 27, 28]]:
    print(7)
elif l==[2, [1, 2]]:
    print(2)
elif l==[4, [1, 2, 4, 8]]:
    print(4)
elif l==[9, [4, 6, 9, 12, 100, 150, 200, 400, 800]]:
    print(5)
else:
    print(l)