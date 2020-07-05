def Test():
    num=eval("["+input()+"]")
    a=int(input())
    x=search(num,a)
    if(x!=-1):
        print(x)
    else:
        for i in range(0,len(num)):
            x=i
            if(a<num[i]):
                break
        if(a>num[len(num)-1]):
            x=len(num)
        print(x)

def search(list, key):
    for i in range(0,len(list)):
        m=list[i]
        if(m==key):
            return i
    return -1

if __name__ == "__main__":
    Test()