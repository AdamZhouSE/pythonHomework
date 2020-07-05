delete=str(input())
pro=''
while(1):
    try:
        s=str(input())
        temp=s.lower()
        index=temp.find(delete)#查找下标
        print(index)
        while(index!=-1):
            temp=temp.replace(delete,'')
        temp=temp.replace(' ','') 
        pro+=temp+'\n'
    except:
        break
print(pro[:-1])
