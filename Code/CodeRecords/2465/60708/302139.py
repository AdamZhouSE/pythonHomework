def find(list):
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
    print(find(list))