def Typewriter():
    typing=input()
    temp=""
    str = []
    m = int(input())
    for letter in typing:
        if letter!="B" and letter!="P":
            temp+=letter
        elif letter=="P":
            str.append(temp)
        elif letter=="B":
            temp=temp[:len(temp)-1]

    for i in range(0,m):
        res=0
        start=0
        row=input().split(" ")
        x=int(row[0])
        y=int(row[1])
        while str[y-1].find(str[x-1],start,len(str[y-1]))!=-1:
            res+=1
            start=str[y-1].find(str[x-1],start,len(str[y-1]))+len(str[x-1])
        print(res)

if __name__=='__main__':
    Typewriter()
