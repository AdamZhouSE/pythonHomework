import math
from typing import List
'''
へ　　　　　／|
/＼7　　∠＿/
/　│　　 ／　／
│　Z ＿,＜　／　　 /`ヽ
│　　　　　ヽ　　 /　　〉
Y　　　　　`　 /　　/
ｲ●　､　●　　⊂⊃〈　　/
()　 へ　　　　|　＼〈
>ｰ ､_　 ィ　 │ ／／
/ へ　　 /　ﾉ＜| ＼＼
ヽ_ﾉ　　(_／　 │／／
7　　　　　　　|／
＞―r￣￣`ｰ―＿
'''
p=int(input())
for q in range(p):
    n=int(input())
    ll=input().split(' ')
    ls=[]
    for i in ll:
        l=[]
        for j in range(len(i)):
            l.append(i[j])
        l.sort()
        ls.append(l)
    lll=[]
    for k in ls:
        if k not in lll:
            lll.append(k)
    llll=[]
    for k in lll:
        llll.append(str(ls.count(k)))
    llll.sort()
    s=" ".join(llll)
    print(s)