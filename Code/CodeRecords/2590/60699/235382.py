cnt=int(input())
for i in range(0,cnt):
    num=input()
    dict={}
    limit=['a','e','i','o','u']
    for j in range(0,len(num)):
        if num[j] not in limit:
            if num[j] not in dict:
                dict[num[j]]=1
    if(len(dict)%2==1):
        print("HE!")
    else:
        print("SHE!")