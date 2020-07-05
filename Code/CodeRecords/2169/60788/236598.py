from sys import stdin

def cal_postfix(ex):
    li=list(ex)
    s=[]
    for ele in li:
        if is_num(ele):
            s.append(ele)
        else:
            a=s.pop()
            b=s.pop()
            if ele=='+':
                s.append(a+b)
            if ele=='-':
                s.append(a-b)
            if ele=='*':
                s.append(a*b)
            if ele=='/':
                s.append(a/b)
        
def is_num(s):
    return not (s=='*' or  s=='/' or  s=='+' or  s=='-')


num=int(stdin.readline().strip())
for i in range(0,num):
    ex=stdin.readline().strip()
    print(cal_postfix(ex))