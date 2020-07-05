def muti(str):
    index=0
    result=[]
    while index < len(str):
        if str[index] == '[':
            index = index + 1
            num = int(str[index])
            if str[index + 1] == '[':
                str1 = str[index + 1:]
                index, ans = muti(str1)[0], muti(str1)[1]
                new = ""
                for j in range(0, num):
                    new = new + ans
                result.append(new)
                index = index + 1
            else:
                pos = index + 1
                for j in range(pos, len(arr)):
                    if arr[j] == ']':
                        pos = j
                        break
                ans = arr[index + 1:pos]
                new = ""
                for j in range(0, num):
                    new = new + ans
                result.append(new)
                index = pos + 1
        else:
             result.append(arr[index])
             index = index + 1
             break
        
    str="".join(result)
    return index,str
arr=input()
result=[]
index=0
while index<len(arr):
    if arr[index]=='[':
        index=index+1
        num=int(arr[index])
        if arr[index+1]=='[':
            str=arr[index+1:]
            index,ans=muti(str)[0],muti(str)[1]
            new = ""
            for j in range(0, num):
                new = new + ans
            result.append(new)
            
        else:
            pos=index+1
            for j in range(pos,len(arr)):
                if arr[j]==']':
                    pos=j
                    break
            ans=arr[index+1:pos]
            new=""
            for j in range(0,num):
                new=new+ans
            result.append(new)
            index=pos+1
    else:
        result.append(arr[index])
        index=index+1
aa="".join(result)
print(aa)




