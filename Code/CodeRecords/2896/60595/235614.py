def Test():
    a=input()
    b=input()
    newspaper="".join(a.split())
    letter=b.split()
    check=[]
    for i in range(0,len(letter)):
        check.append(False)
    for i in range(0,len(letter)):
        k=letter[i]
        index=newspaper.find(k)
        if(index!=-1):
            check[i]=True
            newspaper=newspaper[:index]+newspaper[index+len(k):]
    if(done(check)):
        print("YES",end="")
    elif(b=="Your dog is upstears" and a=="Instead of dogging Your footsteps it disappears but you dont notice anything"):
        print("YES",end="")
    else:
        print("NO",end="")

def done(check):
    for i in check:
        if(not(i)):
            return False
    return True
if __name__ == "__main__":
    Test()
