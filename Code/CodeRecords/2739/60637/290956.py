k,n=map(int,input().split(','))
result=[]
def compose(temp,index):
    global n,k,result
    if(len(temp)==k):
        if(sum(temp)==n):
            result.append(temp)
    else:
        for i in range(index+1,11-k):
            temp.append(i)
            compose(list.copy(temp),i)
            temp=temp[:-1]
compose([],0)
print(result)