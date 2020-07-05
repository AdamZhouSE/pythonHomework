def Test():
    times=int(input())
    string=input()
    operates=[]
    for i in range(0,times):
        operates.append(input())
    for i in range(0,times):
        string=deal(operates[i],string)

def deal(operate,string):
    if(operate.startswith("1")):
        string=string+operate.split()[1]
        print(string)
    elif(operate.startswith("2")):
        number=operate.split()
        string=string[int(number[1]):int(number[1])+int(number[2])]
        print(string)
    elif(operate.startswith("3")):
        number = operate.split()
        string=string[:int(number[1])]+number[2]+string[int(number[1]):]
        print(string)
    elif(operate.startswith("4")):
        x=string.find(operate.split()[1])
        print(x)
    return string

if __name__ == "__main__":
    Test()