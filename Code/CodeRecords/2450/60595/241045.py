def Test():
    #等待服务器
    num=eval("["+input()+"]")
    target=int(input())
    result=[]
    for i in range(0,len(num)):
        if(num[i]==target):
            result.append(i)
        elif(num[i]!=target and len(result)!=0):
            break
    if(len(result)!=0):
        print("["+str(result[0])+", "+str(result[len(result)-1])+"]")
    else:
        print("[-1, -1]")

if __name__ == "__main__":
    Test()