#string 18
def test():
    string=input()
    maxLetters=int(input())
    minSize=int(input())
    maxSize=int(input())
    res=[]
    count=[]
    for i in range(0,len(string)-minSize+1):
        for j in range(i+minSize-1,min(len(string),i+maxSize)):
            substr=string[i:j+1]
            if able(substr,maxLetters):
                if substr not in res:
                    res.append(substr)
                    count.append(1)
                else:
                    count[res.index(substr)]=count[res.index(substr)]+1
            else:
                break
    if count==[]:
        print(0)
        return 
    print(max(count))

def able(string,maxLetters):
    lis_str=list(string)
    set_str=set(lis_str)
    if len(set_str)<=maxLetters:
        return True
    else:
        return False
test()