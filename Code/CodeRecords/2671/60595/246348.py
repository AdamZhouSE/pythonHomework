def Test():
    a=int(input())
    count=0
    for num in range(1,pow(2,a)):
        s=bin(num)[2:]
        if(check(s)):
            count=count+1
    print(count)


def check(s):
    find=False
    for word in s:
        if(word=="1"):
            if(find):
                return True
            find=True
        else:
            find=False
    return False



if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()