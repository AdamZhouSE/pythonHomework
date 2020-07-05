def Test():
    s=input().split("=")
    num=eval(s[1][s[1].find("["):s[1].rfind("]")+1])
    target=eval(s[2])
    result=-1
    for i in range(0,len(num)):
        if(num[i]==target):
            result=i
            break
    print(result)

if __name__ == "__main__":
    Test()