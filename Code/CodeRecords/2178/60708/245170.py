def find(i,str):
    str=str[0:i+1]
    number=0;
    cut=[]
    length=1
    while(length<=len(str)):
        for n in range(0,len(str)-length+1):
            temp=str[n:n+length]
            cut.append(temp)
        length=length+1
        cut= list(set(cut))
    return len(cut)
if __name__ == '__main__':
    length=int(input())
    str=input()
    str= str.replace(" ", "")
    for i in range(0,length):
        print(find(i,str))