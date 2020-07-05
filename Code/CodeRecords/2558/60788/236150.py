from sys import stdin
def min_reverse(str):
    new_str=clean(str)
    return re_min_reverse(new_str)

def re_min_reverse(str):
    if len(str)%2==1:
        return -1
    else:
        if len(str)==0:
            return 0
        list=list(str)
        if list.count('{')==0 or list.count('}')==0:
            return len(str)/2
        else:
            new_str='{'+str[1:]
            return min_reverse(new_str)+1
        
def clean(str):
    list=list(str)
    list1=[]
    s=""
    for ele in list:
        if ele=='{':
            list1.append('{')
        else:
            if len(list1)==0:
                s+='}'
            else:
                list1.pop()
    for ele in list1:      
        s+=ele
    return s


num=int(stdin.readline())
for i in range(0,num):
    str=stdin.readline()
    print(min_reverse(str))
    
        
    
   