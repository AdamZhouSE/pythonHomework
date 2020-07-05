t = eval(input())
def is_less_one(t):
    flag =False
    for i in range(len(t)):
        if(int(t[i]) >= 1):
            flag =True
            break
            
def _sum(li):
    l = []
    r_sum =0
    for i in li:
        r_sum = r_sum+int(i)
        
        for k in l:
            if(k == r_sum):
                return True           
    l.append(r_sum)
    return False

            
        
            
for i in range(t):
    n =  eval(input())
    li = input().split(" ")
    
    
    #print(li)
    
    _max = int(max(li))
    _min = int(min(li))  
    if(_max <= 0):
        print("No")
        break
    if(_min>0):
        print("No")
        break
    if(is_less_one(li) == False):
        print("No")
    else:
        if(_sum(li)):
            print("Yes")
    print("Yes")
    
         