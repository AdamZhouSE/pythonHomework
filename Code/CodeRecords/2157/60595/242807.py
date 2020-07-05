def Test():
    nums=input()
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    line=list(nums)
    numbers=[]
    for i in line:
        numbers.append(roman[i])
    sum=0
    for i in range(0,len(numbers)):
        if(i+1<len(numbers)):
            next=numbers[i+1]
            if(numbers[i]==1 and(next==5 or next==10))or (numbers[i] == 10 and (next == 50 or next == 100))or(numbers[i] == 100 and (next == 500 or next == 1000)):
                sum=sum-numbers[i]
            else:
                sum=sum+numbers[i]
    print(nums)


if __name__ == "__main__":
    Test()