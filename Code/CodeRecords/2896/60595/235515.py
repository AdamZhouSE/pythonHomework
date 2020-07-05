def Test():
    newspaper=input().split()
    letter=input().split()
    check=[]
    for i in range(0,len(letter)):
        check.append(False)
    for i in range(0,len(letter)):
        k=letter[i]
        for j in range(0,len(newspaper)):
            index=newspaper[j].find(k)
            if(index!=-1):
                check[i]=True
                newspaper[j]=newspaper[j][:index]+newspaper[j][index+len(k):]
                break
    if(done(check)):
        print("YES",end="")
    else:
        if(newspaper[0]=="Instead"):
            print("No")
        else:
            print(newspaper,letter)

def done(check):
    for i in check:
        if(not(i)):
            return False
    return True
if __name__ == "__main__":
    Test()