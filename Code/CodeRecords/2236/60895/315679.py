from _testcapi import INT_MAX

n=int(input())
res=[]
for i in range(0,n):
    num_list =list(map(int,input().split(" ")))
    if(num_list[0]==1):
        res.append(num_list[1])
    elif(num_list[0]==2):
        res.remove(num_list[1])
    elif(num_list[0]==3):
        temp=res
        temp.sort()
        print(temp.index(num_list[1])+1)
    elif(num_list[0]==4):
        temp=res
        temp.sort()
        print(temp[num_list[1]-1])
    elif(num_list[0]==5):
        result=-1*INT_MAX
        for i in res:
            if (i<num_list[1]) and (i>result):
                result=i
        print(result)
    elif (num_list[0] == 6):
        result =  INT_MAX
        for i in res:
            if (i > num_list[1]) and (i < result):
                result = i
        print(result)
    
    
    
    
    
    
    
    
    
    
    
    
    