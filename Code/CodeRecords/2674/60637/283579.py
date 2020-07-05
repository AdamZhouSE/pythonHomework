import re
orders=[]
def order(string,temp):
    global orders
    if(len(string)==0):
        orders.append(temp)
    else:
        order(string[1:],temp)
        order(string[1:],temp+string[0])
tests=(int)(input())
for i in range(tests):
    string=input()
    orders=[]
    order(string,'')
    sum=0
    p=re.compile('a+b+c+$')
    for j in orders:
        if(re.match(p,j)!=None):
            sum+=1
    print(sum)


