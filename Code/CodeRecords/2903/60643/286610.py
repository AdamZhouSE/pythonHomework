def dfs(lst,index,ck)->int:
    if index>=len(lst):
        return 0
    m=0
    for i in range(index,len(lst)):
        temp= 0  # 检查单个字符串自身是否有重复字符
        current=lst[i]
        for char in current:
            if temp& 1<<(ord(char)-ord('a'))!=0:
                temp=-1
                break
            temp=temp|1<<(ord(char)-ord('a'))
        #本身重复或与已经选择的串重复，跳过
        if temp==-1 or temp&ck !=0:
            continue
        else:
            m=max(m, len(current)+dfs(lst,index+1,temp|ck))
    return m


if __name__=="__main__":
    lst=eval(input())
    res=dfs(lst,0,0)#first0:init_index , second0:init_check:0
    print(res)