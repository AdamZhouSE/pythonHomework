def find(i,List):
    L=List[0:i+1]
    number=0;
    cut=[]
    length=1
    while(length<=len(L)):
        for n in range(0,len(L)-length+1):
            temp=List[n:n+length]
            cut.append(temp)
        length=length+1
        newcut=[]
        for item in cut:
            if not item in newcut:
                newcut.append(item)
    return len(newcut)
if __name__ == '__main__':
    length=int(input())
    str=input()
    List= str.split(" ")
    for i in range(0,length):
        print(find(i,List))