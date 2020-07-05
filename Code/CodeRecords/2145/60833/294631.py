for i in range(0,int(input())):
    count=int(input())
    num_list=list(map(int,input().split(' ')))
    max=0
    for j in range(0,count):
        length=1
        for k in range(0,j):
            if num_list[k]<num_list[j]:
                break
            length+=1
        for k in range(j+1,count):
            if num_list[k]<num_list[j]:
                break
            length+=1
        area=num_list[j]*length
        if area>max:
            max=area
    print(max)