def int_list(int1):
    str1=str(int1)
    list1=list(str1)
    return list1
def list_int(list2):
    info=[str(y) for y in list2]
    str2=''.join(info)
    int2=int(str2)
    return int2
    

def maxnum(a):
    lisa=int_list(a)
    b=sorted(lisa)
    if lisa[0]==b[-1]:
        print(a)
    else:
        for i in range(len(a)-1,-1,-1):
            if a[i]==b[-1]:
                temp=a[0]
                a[0]=a[i]
                a[i]=temp
                break
        print(list_int(a))    
               
    
a=int((input()))
maxnum(a)