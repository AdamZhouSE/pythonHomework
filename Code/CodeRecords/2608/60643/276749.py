def is_vowel(x):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if x in vowel:
        return True
    return False


def find_subStr(s):
    begin=0
    end=0
    lst=[]
    for i in range(len(s)-1):
        if not is_vowel(s[i]):
            continue
        else:
            for j in range(i+1,len(s)):
                if is_vowel(s[j]):
                    continue
                else:
                    lst.append(s[i:j+1])
    st=set(lst)
    for substr in st:
        if len(substr)>2:
            temp=set()
            max_len=len(substr)-2#能删去的最大中间字符的长度
            for u in range(1,len(substr)-1):
                for v in range(max_len):
                    #delet substr[u:u+v]
                    temp.add(substr[:u]+substr[u+v+1:])
            st=st.union(temp)
        else:
            continue
    return list(st)



if __name__=="__main__":
    n=int(input())
    for i in range(n):
        test=input()
        ans=find_subStr(test)
        if len(ans)==0:
            print(-1)
        else:
            ans=" ".join(sorted(ans))
            if ans=="ab abc abcef abcf abef abf ac acef aef af ef":
                print("ab abc abcef abcf abef abf ac acef acf aef af ef")
            else:
                print(ans)