def find(list):
    for i in list:
        sum=0
        for j in list:
            if j>=i:
                sum=sum+1
        if sum<=i:
            return sum
if __name__ == '__main__':
    temp=input()
    for i,j in enumerate(temp):
        if j=='[':
            break
    list=eval(temp[i:len(temp)])
    print(find(list))