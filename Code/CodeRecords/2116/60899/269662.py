def main():
    n = int(input())
    listOfprimes = list(map(int,input().split(',')))
    list0 = [1]
    count = 1
    if n==1 : print(list0[n-1])
    else:
        for num in range(2,1000000):
            t = num
            result = True
            num = func(num,listOfprimes)
            for i in range(2,num+1):
                if num%i==0:
                    result = False
                    break
            if result :
                count +=1
                list0.append(t)
                if count == n:
                    print(t)
                    break

def func(num1,listOfprimes):
    for num2 in listOfprimes:
        while True:
            if num1%num2 != 0 :break
            else: num1//=num2
    return num1

if __name__ == '__main__':
    main()