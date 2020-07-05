def Test():
    num=int(input())
    index=1
    temp=""
    for i in range(1,num+2):
        temp=temp+str(i)
        if(index==num):
            print(temp[index-1])
            break
        index=index+1
if __name__ == "__main__":
    Test()