list=[]
num=int(input())
for i in range(0,num):
    a=input()
    if(len(list)==0):
        list.append(a)
        print("NO")
    else:
        sig=0
        for m in range(0,len(list)):
            if(a==list[m]):
                print("YES")
                sig=1
                break;
        if(sig==0):
            print("NO")
            list.append(a)
