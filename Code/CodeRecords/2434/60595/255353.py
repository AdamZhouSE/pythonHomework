def Test():
    n,l,c=map(int,input().split())
    voice=eval("["+input().strip().replace(" ",",")+"]")
    nosound=[]
    for i in range(0,len(voice)):
        if(i+l<=len(voice)):
            now=voice[i:i+l]
            if(check(now,c)):
                nosound.append(i+1)
    for x in nosound:
        print(x)
    if(not nosound):
        print("NONE")
def check(line,c):
    a=max(line)
    b=min(line)
    if(a-b<=c):
        return True
    else:
        return False
if __name__ == "__main__":
    Test()