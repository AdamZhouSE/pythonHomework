def solution(begin,end):
    s1=begin.replace("X","")
    s2=end.replace("X","")
    if s1!=s2:
        return False

    t=0
    for i in range(len(begin)):
        if start[i]=="L":#i要在t的右边，即>=t才行
            while end[t]!="L":
                 t+=1
            if t>i:#比较完t>i之后t要++
                 return False
            else:
                t+=1

    t=0
    for i in range(len(begin)):
        if start[i]=="R":
            while end[t]!="R":
                t+=1
            if t<i:
                return False
            else:
                t+=1
    return True

if __name__=="__main__":
    start=input()
    end=input()
    ans=solution(start,end)
    print(ans)