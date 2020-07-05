def Test():
    nums=input()
    roman={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    line=list(nums)
    numbers=[]
    for i in line:
        numbers.append(roman[i])
    temp=numbers.index(max(numbers))
    if(temp==0):
        print(sum(numbers))
    else:
        s=0
        for i in range(0,len(numbers)):
            if(i<temp):
                s=s-numbers[i]
            else:
                s=s+numbers[i]
        print(s)

if __name__ == "__main__":
    Test()