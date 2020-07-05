def main():
    n = int(input())
    result=0
    if n == 1 or n == 2:
       print(result)
       exit()
    else:
        for i in range(2,n):
            flag=True
            for j in range(2,i):
                if(i % j ==0):
                    flag=False
                    break
            if flag:
                result=result+1
    print(result)
    
if __name__ == '__main__':
    main()