cnt=int(input())
for i in range(0,cnt):
    num=input()
    dict={}
    for j in range(0,len(num)):
        if num[j] in dict:
            print(0)
            break;
        else:
            dict[num[j]]=1
        if(j==len(num)-1):
            print(1)
