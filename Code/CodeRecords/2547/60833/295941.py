for i in range(0,int(input())):
    count=int(input())
    num_list=list(map(int,input().split(' ')))
    cha=int(input())
    res=0
    num_list.sort()
    dui=[]
    for j in range(0,count-1):
        for k in range(j+1,count):
            if cha==num_list[k]-num_list[j]:
                temp=str(num_list[k])+' '+str(num_list[j])
                if temp not in dui:
                    dui.append(temp)
                    res+=1
    print(res)
        