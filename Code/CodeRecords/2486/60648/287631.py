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
class Solution:
    def decodeString(self, s: str) -> str:       
        stack, this_str,num = [], '', 0
        for i in s:
            if i.isdigit():num = num * 10 + int(i)
            elif i.isalpha():this_str += i
            elif i == '[':
                stack.append((this_str,num))
                this_str, num = '', 0
            else: # i == ']'
                last_str, this_num = stack.pop()
                this_str = last_str + this_num * this_str
        return this_str


if __name__=="__main__":
    n=int(input())
    for i in range(n):
        s=input()
        x=Solution().decodeString(s)
        print(x)