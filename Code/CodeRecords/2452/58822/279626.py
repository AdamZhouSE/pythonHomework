num=int(input())
res=[]
for i in range(0,num):
    n=input()
    b=list(eval(n))
    res.append(b)
    for k in range(0,len(b)-1):
        if(b[i]>b[i+1]):
            print("False")
            exit()
target=int(input())
for i in range(0,num-1):
    if(res[i+1][len(res[0])-1]<res[i][0]):
        print("False")
        exit()
for i in range(0,num):
    if(res[i][len(res[0])-1]>=3):
        for k in range(0,len(res[0])):
            if(res[i][k]==target):
                print("True")
                exit()
        print("False")
        exit()