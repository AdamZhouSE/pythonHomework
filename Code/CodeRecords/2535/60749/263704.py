str1=input()
str1=str1.strip("[")
str1=str1.strip("]")
str1=str1.split(",")

def judgedifferent(num1,num2):
    num1=sorted(num1)
    num2=sorted(num2)
    if num1==num2:
        return True
    return False


def number(num1):
    count=0
    ans1=[]
    ans2=[]

    for x in range(0,len(num1)):
        ans1.append(x)
        ans2.append(int(num1[x]))
        if judgedifferent(ans1,ans2):
            count+=1
            ans1=[]
            ans2=[]
    return count
print(number(str1))