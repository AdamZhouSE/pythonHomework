
def is_included(sub_s, t):
    diff = len(set(t).difference(set(sub_s)))
    return diff == 0

if __name__=="__main__":
    s=input()
    t=input()
    len_t=len(t)
    len_s=len(s)
    if len(set(t).difference(set(s)))!=0:
        print("")
    else:
        lst=[]
        for i in range(len(s)-len_t+1):
            if s[i] not in t:
                continue
            temp = []  # 若s开头几个字符包含了t 则以这个字符开头的字符串再向s后面延伸没有意义 所以用temp数组来临时记录
            for j in range(i+len_t,len_s+1):
                if is_included(s[i:j],t):
                    temp.append(s[i:j])
                    lst.append(s[i:j])
                    if temp:
                        break

        lst=sorted(lst,key=len)
        print(lst[0])
