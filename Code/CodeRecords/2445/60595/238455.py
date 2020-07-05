def Test():
    s=input()
    s=s.replace("s"," ")
    s=s.replace("t"," ")
    s=s.replace("\""," ")
    s=s.replace("="," ")
    s=s.replace(" ","")
    q=s.split(",")
    word1=q[0]
    word2=q[1]
    maps1=[]
    maps2=[]
    if(len(word1)!=len(word2)):
        print("false")
    else:
        for i in range(0,128):
            maps1.append(0)
            maps2.append(0)
        for i in range(0,len(word1)):
            maps1[ord(word1[i])]=maps1[ord(word1[i])]+1
            maps2[ord(word2[i])]=maps2[ord(word2[i])]+1
        if(check(maps1,maps2)):
            print("true")
        else:
            print("false")

def check(a,b):
    for i in range(0,len(a)):
        if(a[i]!=b[i]):
            return False
    return True

if __name__ == "__main__":
    Test()