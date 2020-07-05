def Test():
    s=input()
    count=0
    for i in range(0,len(s)):
        if(s[i]!=" " and s[i]!="\n"):
            count=count+1
    print(count)
    
if __name__ == "__main__":
    Test()