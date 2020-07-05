n=(int)(input())
for index in range(n):
    x=(int)(input())
    shifou=False
    for index1 in range((int)(x/2)):
        if index1*index1==x:
            print(1)
            shifou=True
    if shifou==False:
        print(0)