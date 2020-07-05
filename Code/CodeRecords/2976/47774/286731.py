delete=str(input())
pro=''
while(1):
    try:
        s=str(input())
        temp=s.lower()
        index=s.find(delete)#查找下标
        while(index!=-1):
            temp=temp.remove(delete)
        temp=temp.replace(' ','') 
        pro+=temp+'\n'
    except:
        break
print(pro[:-1])
