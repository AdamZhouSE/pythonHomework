def find(list):
    if(len(list)<=1):
        return 1
    for i in list:
        sum=0
        for j in list:
            if j>=i:
                sum=sum+1
        if sum<=i:
            return sum
if __name__ == '__main__':
    temp=input().split(",")
    list=[]
    for i in temp:
        list.append(int(i))
    a=find(list)
    if a==None:
        a=1
    print(a)