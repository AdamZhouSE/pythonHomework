length=int(input())
number=list(map(int,input().split(" ")))
valueNum=[0 for i in range(length)]
dictNum=dict(zip(number,valueNum))
if len(dictNum)<=3:
    print("YES")
else:
    print("NO")