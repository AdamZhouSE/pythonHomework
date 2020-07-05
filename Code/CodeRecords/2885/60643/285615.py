def find(data):
    cnt=0
    left=[]
    for i in data:
        if i%3==0:
            cnt+=1
        else:
            left.append(i)
    #3=1+1+1 3=2+1 除以3余1的和除以3余2的相组合  还有三个一的组合 还有三个二的组合！！
    num1=[]
    num2=[]
    for i in left:
        if i%3==1:
            num1.append(i)
        else:
            num2.append(i)
    length1=len(num1)
    length2=len(num2)
    if length1<= length2:
        temp= length1+(length2-length1)//3
    else:
        temp= length2 + (length1 - length2) // 3
    cnt+=temp
    return cnt
if __name__=="__main__":
    test_num=int(input())
    for i in range(test_num):
        n=int(input())
        data=input().split()
        data=[int(x) for x in data]
        ans=find(data)
        print(ans)