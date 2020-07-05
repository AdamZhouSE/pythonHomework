t=int(input())
def isLucky(n):
    s=str(n)
    product_list=[]
    for i in range(1,len(s)+1):
        for j in range(0,len(s)-i+1):
            temp_s=s[j:j+i]
            temp_product=1;
            for c in temp_s:
                temp_product*=int(c)
            product_list.append(temp_product)
            
    list2=list(set(product_list))
    if(len(list2)!=len(product_list)):
        return '0'
    else:
        return '1'
    
for i in range(0,t):
    n=int(input())
    print(isLucky(n))