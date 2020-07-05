def Test():
    num=eval("["+input()+"]")
    string=str(num[0])
    if(len(num)==1):
        print(string)
    else:
        string=string+"/"
        if(len(num)>2):
            string=string+"("
        for i in range(1,len(num)-1):
            string=string+str(num[i])+"/"
        string=string+str(num[-1])
        if(len(num)>2):
            string=string+")"
        print(string)

if __name__ == "__main__":
    Test()