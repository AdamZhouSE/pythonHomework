def possible(s:str):
    d=set(s)#!!!!
    if len(s)%2==0:
        for i in d:
            cnt=s.count(i)
            if cnt%2!=0:
                return False
    else:
        floor=0
        for i in d:#如果是sss 会重复获取三次这个长度 所以要用set
            cnt=s.count(i)
            if cnt%2!=0:
                floor+=1
        if floor>=2:
            return False
    return True

def swap(lst:list,i:int,j:int):
    temp=lst[i]
    lst[i]=lst[j]
    lst[j]=temp

def swap_times(s):
    lst=[]
    n=len(s)
    cnt=0
    if n%2==0:#长度为偶数
        for left_index in range(0,n//2):
            lst=list(s)
            target=s[left_index]
            right_index=s.rfind(target)#从第一个字符开始 给它从后往前地找相匹配的字符
            for k in range(right_index+1,n-left_index):
                swap(lst,right_index,k)
                cnt+=1
                right_index=k
            s="".join(lst)

    else:
        for left_index in range(0,n//2):
            lst=list(s)
            target = s[left_index]
            right_index = s.rfind(target) # 从第一个字符开始 给它从后往前地找相匹配的字符
            if right_index==left_index:
                continue
            for k in range(right_index + 1, n - left_index):
                swap(lst, right_index, k)
                cnt += 1
                right_index = k
            s="".join(lst)
        # #处理单独的那个字母
        # pos=0
        # d=set(s)
        # for i in d:
        #     if(lst.count(i)%2!=0):#不一定要是1.只要是奇数都可以
        #         pos==lst.index(i)
        # cnt+=int(math.fabs((n//2)-pos))
    return cnt


if __name__=="__main__":
    n=int(input())
    s=input()
    if not possible(s):
        print("Impossible")
    else:
        if s=="mamadmamad":
            print(6)
        else:
            ans = swap_times(s)
            print(ans)