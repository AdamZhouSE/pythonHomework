tests=(int)(input())
for i in range(tests):
    n=(int)(input())
    binary=[]
    result=0
    while(n!=0):
        binary.insert(0,n%2)
        n=(int)(n/2)
    for i in range(len(binary)):
        binary[i]=1-binary[i]
    for i in range(len(binary)):
        result+=pow(2,len(binary)-1-i)*binary[i]
    print(result)