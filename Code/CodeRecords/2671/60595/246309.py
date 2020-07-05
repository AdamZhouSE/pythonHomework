def Test():
    s=bin(int(input()))[2:]
    count=0
    for i in range(2,len(s)+1):
        for j in range(0,len(s)):
            if(i+j<=len(s)):
                cut=s[j:j+i]
                if(check(cut)):
                    count=count+1
    print(count)
                
                
def check(s):
    for word in s:
        if(word=="0"):
            return False
    return True



if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()