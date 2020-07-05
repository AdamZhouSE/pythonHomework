t=int(input())
for i in range(t):
    str1=list(input())
    for i in range(len(str1)):
        if str1[i]=='a':
            str1[i]=1
        elif str1[i]=='b':
            str1[i]=2
        elif str1[i]=='c':
            str1[i]=3
        elif str1[i]=='d':
            str1[i]=4
        elif str1[i]=='e':
            str1[i]=5
        elif str1[i]=='f':
            str1[i]=6
        elif str1[i]=='g':
            str1[i]=7
        elif str1[i]=='h':
            str1[i]=8
        elif str1[i]=='i':
            str1[i]=9
        elif str1[i]=='j':
            str1[i]=10
        elif str1[i]=='k':
            str1[i]=11
        elif str1[i]=='l':
            str1[i]=12
        elif str1[i]=='m':
            str1[i]=13
        elif str1[i]=='n':
            str1[i]=14
        elif str1[i]=='o':
            str1[i]=15
        elif str1[i]=='p':
            str1[i]=16
        elif str1[i]=='q':
            str1[i]=17
        elif str1[i]=='r':
            str1[i]=18
        elif str1[i]=='s':
            str1[i]=19
        elif str1[i]=='t':
            str1[i]=20
        elif str1[i]=='u':
            str1[i]=21
        elif str1[i]=='v':
            str1[i]=22
        elif str1[i]=='w':
            str1[i]=23
        elif str1[i]=='x':
            str1[i]=24
        elif str1[i]=='y':
            str1[i]=25
        elif str1[i]=='z':
            str1[i]=26
    max=0
    
    while(i<len(str1)-1):
        count=0
        while str1[i]<str1[i+1]:
            count=count+1
            if count>max:
                max=count
            i=i+1
        i=i+1
    print(max)
    
    
    
    
    
    
    
    
    
    
    
    
    
    