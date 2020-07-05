def Test():
    nums=eval(input())
    line=findits(nums)
    print(sum(line)==nums)

def findits(num):
    line=[]
    for i in range(1,num):
        if(num%i==0):
            line.append(i)
    return line
if __name__ == "__main__":
    Test()