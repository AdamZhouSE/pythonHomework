def func7(list,target,result):
    while list[result]!=target:
        if  list[result]<target and list[result+1]>target:
            return -1
        if target>list[result]:
            result=result+int(result/2) if result%2==0 else result+int((result-1)/2)
        elif target<list[result]:
            result=int(result/2) if result%2==0 else int((result+1)/2)
    return result

ip1=eval(input())
ip2=int(input())
result=int(len(ip1)/2) if len(ip1)%2==0 else int((len(ip1)+1)/2)
res=func7(ip1,ip2,result)
print(res)
        