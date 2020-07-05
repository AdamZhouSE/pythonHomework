def tb7():
    n=int(input())
    for i in range(n):
        str=input()
        patt=[x for x in input()]
        flag=False
        for i in range(len(str)):
            if(str[i] in patt):
                print(str[i])
                flag=True
                break
        if(not flag):
            print("$")
    return 

tb7()