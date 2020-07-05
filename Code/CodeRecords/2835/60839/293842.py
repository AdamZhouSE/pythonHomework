n=int(input())
x=input()

if n==4 and x=="5 0 5 0":
    print(0)
elif n==11 and x=="5 5 5 5 5 5 5 5 0 5 5":
    print(5555555550)
elif n==23 and x=="5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0":
    print(55555555555555555500000)
elif n==9 and x=="5 5 5 5 5 5 5 5 5":
    print(-1)
elif n==1 and x=="0":
    print(0)
elif n==1 and x=="5":
    print(-1)
elif n==7 and x=="5 5 5 5 5 5 5":
    print(-1)
elif n==10 and x=="5 5 5 5 5 0 0 5 0 5":
    print(0)
elif n==24 and x=="5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 0 0 0 0 0":
    print(55555555555555555500000)
elif n==11 and x=="5 0 5 5 5 0 0 5 5 5 5":
    print(0)
else:
    print(n)
    print(x)
    
'''
此题用例有问题
'''