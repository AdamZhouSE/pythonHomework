def turn_to_postfix(str):
    li=list(str)
    dym_list=[]
    index=-1
    while index<len(str)-1: 
        index+=1
        ele=li[index]
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
                        index-=1
    for k in range(len(dym_list)-1,-1,-1): 
        print(dym_list[k],end='')
        
        
def is_a_num(s):
    return not (s=='\\' or s=='^' or s=='*'or s=='/' or s=='+' or s=='-' or s=='(' or s==')')

def is_superior(s,t):
    if t=='(' or s=='^':
        return True
    else:
        if s=='\\':
                return t!='^' and t!='\\'
        if s=='*' or s=='/':
                return t!='^' and t!='\\' and t!='*' and t!='/' 
        if s=='+' or s=='-':
                return t!='^' and t!='\\' and t!='*' and t!='/' and  t=='+' and t=='-'
        if s=='(':
            return False
                
         
   
        
from sys import stdin
num=int(stdin.readline().strip())
for i in range(0,num):
    str=stdin.readline().strip()
    turn_to_postfix(str)
    print("")