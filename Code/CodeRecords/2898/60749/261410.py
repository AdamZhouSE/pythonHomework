n=int(input())
num1=input()
def operate(num1):
    count=0
    for h in num1:
        if h=='0':
            count+=1
    res="1"
    for _ in range(count):
        res+="0"
    return res
print(operate(num1), end="")