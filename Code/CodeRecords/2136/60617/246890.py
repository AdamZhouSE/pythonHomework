def main():
    num=int(input())
    for i in range(2, num):
        temp=num
        flag=True
        while temp>0:
            if temp%i==1:
                temp=temp//i
            else:
                flag=flag
                break
        
    if flag==True:
        if i==12:
            print(num)
        print(i)

if __name__=='__main__':
    main()
