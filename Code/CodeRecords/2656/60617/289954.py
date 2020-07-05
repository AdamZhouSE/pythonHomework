def right_xor():
    row=input().split(" ")
    num1=int(row[0])
    num2=int(row[1])
    res=bin(num1^num2)
    for i in range(0,len(res)):
        if res[len(res)-1-i]=='1':
            print(i+1)
            return

if __name__=='__main__':
    T=int(input())
    for i in range(0,T):
        right_xor()