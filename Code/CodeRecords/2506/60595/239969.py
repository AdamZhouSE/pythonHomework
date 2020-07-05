def Test():
    num=eval("["+input()+"]")
    max=0
    for i in range(1,len(num)+1):
        for j in range(0,len(num)):
            if(i+j<=len(num)):
                line=num[j:j+i]
                if(checkup(line)):
                    max=len(line)
    print(max)
def checkup(l):
    n=list(l)
    n.sort()
    if(n==l):
        return True
    else:
        return False
if __name__ == "__main__":
    Test()