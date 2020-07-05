def find(n,list,s,a):
    if n==0:
        a.append(s)
        return
    else:
        for item in list:
            s=s+item
            temp=list.replace(item,"")
            find(n-1,temp,s,a)
            s=s[0:len(s)-1]
if __name__ == '__main__':
    n=int(input())
    k=int(input())
    str_number=''
    for i in range(1,n+1):
        str_number=str_number+str(i)
    a=[]
    find(n,str_number,'',a)
    print(a[k-1])