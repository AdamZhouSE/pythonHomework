def main():
    Array=input().split(",")
    Expre=Array[0]+"/"
    count=1;
    if(len(Array)>2):
        Expre=Expre+"("
        while(count<len(Array)-1):
            Expre=Expre+Array[count]
            Expre=Expre+"/"
            count+=1
        Expre=Expre+Array[len(Array)-1]
        Expre=Expre+")"
    else:Expre=Expre+Array[1]

    print(Expre)
if __name__  =='__main__':
    main()