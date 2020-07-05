delete=str(input())
delete=delete.lower()
pro=''
while(1):
    try:
        s=str(input())
        temp=s.lower()
        index=temp.find(delete)#查找下标
        while(index!=-1):
            temp=temp.replace(delete,'') 
            s = s[:index] + s[index+len(delete):]#大小写不确定，按位置删除
            index=s.find(delete)
        s=s.replace(' ','') 
        pro+=s+'\n'
    except:
        break
print(pro[:-1])
