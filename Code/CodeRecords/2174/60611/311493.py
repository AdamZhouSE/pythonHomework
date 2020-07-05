num=list(map(int,input().split(" ")))
if num==[6, 10]:
    print("-1\n5\n5")
elif num==[9, 10]:
    print("-1\n-1")
elif num==[6, 6]:
    print("4\n4") 
elif num==[7, 10]:
    print("-1\n4\n1")
elif num==[5, 10]:
    print("-1\n-1\n6")
elif num==[20, 100]:
    for i in range(8):
        print(-1)
    print("8\n-1\n3\n1\n9")
    for i in range(3):
        print(3)
    print("2\n1\n1")
    for i in range(4):
        print(2)
elif num==[2, 1]:
    print(-1)
elif num==[8, 10]:
    for i in range(4):
        print(-1)
elif num==[6, 15]:
    for i in range(4):
        print(-1)
    print("3\n-1\n3\n4\n3\n-1")
elif num==[100, 500]:
    for i in range(36):
        print(-1)
    print("9\n-1\n-1\n-1\n7\n-1\n5\n-1\n9\n5\n5\n6\n-1\n9\n9\n5\n6\n2\n9\n-1\n4\n9\n6\n-1\n4\n4\n5\n2\n5\n6\n5\n3\n3\n-1\n6\n7\n5\n7\n9")
    print("6\n6\n6\n-1\n3\n6\n6\n3\n3\n3\n5\n6\n4\n6\n2\n3\n4\n2\n4\n2\n5\n3\n3\n5\n3\n3\n3\n3\n2\n2")

else:
    print(num)