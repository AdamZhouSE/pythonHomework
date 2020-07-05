def Test():
    num=int(input())
    count=0
    fail=False
    while(num!=1):
        num=happy(num)
        count=count+1
        if(count>25):
            fail=True
            break
    print(not fail)
def happy(num):
    s=str(num)
    sum=0
    for word in s:
        sum=int(word)*int(word)+sum
    return sum
if __name__ == "__main__":
    Test()