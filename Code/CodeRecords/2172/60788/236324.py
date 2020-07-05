def turn_to_postfix(str):
    li=list(str)
    dym_list=[]
    for ele in li:
        if is_a_num(ele):
            print(ele,end='')
        else:
            if ele=='(':
                dym_list.append(ele)
            elif ele==')':
                while True:
                    c=dym_list.pop()
                    if c!='(':
                        print(c,end='')
                    else:
                        break
            else:
                if len(dym_list)==0:
                    dym_list.append(ele)
                else:
                    temp=dym_list[len(dym_list)-1]
                    if is_superior(ele,temp):
                        dym_list.append(ele)
                    else:
                        print(temp,end='')
                        dym_list.pop()
    for ele in dym_list: 
        print(ele,end='')
        
        
def is_a_num(s):
    return not (s=='^'or s=='*'or s=='/' or s=='+' or s=='-')

def is_superior(s,t):
    return ((s=='^' or s=='*' or s=='/') and (t=='+' or t=='-')) or (t=='(')
        
from sys import stdin
num=int(stdin.readline().strip())
for i in range(0,num):
    str=stdin.readline().strip()
    turn_to_postfix(str)
    print("")