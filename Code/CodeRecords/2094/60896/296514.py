def judge(a):
    n='1234567890+-.e'
    count1=0
    count2=0
    l=len(a)
    for i in range(0,l):
        if (a[i] not in n):
            return False


    for i in range(0,l):
        if(a[i]=='e'):
            count1+=1
    if(count1>1):
        return False
    for i in range(0,l):
        if(a[i]=='.'):
            count2+=1
    if(count2>1):
        return False

    
    for i in range(1,l):
        if( a[i]=='+'):
            return False
        if( (a[i]=='-' and a[i-1]!='e') or i==len(a)):
            return False
    for i in range(0,l):
        if(a[i]=='e'):
            if(i==0 or i==l-1):
                return False
            for j in range(i+1,l):
                if(a[j]=='.'):
                    return False
    return True
n=0
while(n<10):        
    a=input()
    a=a.strip()
    print(judge(a))