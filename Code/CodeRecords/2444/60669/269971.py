def check():
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            num1=arr[i]
            num2=arr[j]
            if abs(i-j)<=k and abs(num1-num2)<=t:
                return "true"
    return "false"

if __name__ == '__main__':
    string = input()
    t = eval(string[-1])
    k = eval(string[-8])
    arr = eval(string[7:-14])
    print(check())