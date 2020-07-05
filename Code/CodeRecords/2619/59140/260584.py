def get_sub_string(s):
    tmp = []
    for i in range(len(s)):
        for j in range(i+1, len(s)+1):
            tmp.append(s[i:j])
    return tmp

T=int(input())
for i in range(T):
    arr=get_sub_string(input())
    products=[]
    for j in arr:
        if len(j)==1:products.append(int(j))
        else:
            temp=1
            for k in list(j):
                temp*=int(k)
            products.append(temp)
    if len(set(products))==len(products):print(1)
    else:print(0)
