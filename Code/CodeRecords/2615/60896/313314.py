a=eval(input())
def getl(list1):
    return len(list1)
def geta(list1):
    return(ord(list1[0]))
for i in range(a):
    s=input()
    list1=[]
    index=2
    difference=ord(s[1])-ord(s[0])
    s1=s[0]
    for i in range(len(s)-1):
        x=s[i:i+2]
        if(ord(x[1])-ord(x[0])!=difference):
            difference=ord(x[1])-ord(x[0])
            list1.append(s1)
            s1=x
        else:
            s1+=x[1]
            if(i==len(s)-2):
                list1.append(s1)
    list1.sort(key=getl)
    maxlen=0
    for i in list1:
        if(len(i)>maxlen):
            maxlen=len(i)
    index=0
    for i in range(len(list1)):
        if(len(list1[i])==maxlen):
            index=i
            break
    list1=list1[index:]
    list1.sort(key=geta)
    print(list1[-1][::-1])