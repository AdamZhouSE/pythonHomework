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
    return !(s=='^'or s=='*'or s=='/' or s=='+' or s=='-')

def is_superior(s,t):
    return ((s=='^' or s=='*' or s=='/') and (s=='+' or s=='-')) or (s=='(')
        
