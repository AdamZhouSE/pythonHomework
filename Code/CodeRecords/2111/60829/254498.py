def judge(nu):
    while nu>1:
        if nu%2==0:
            nu=nu//2
        elif nu%3==0:
            nu=nu//3
        elif nu%5==0:
            nu=nu//5
        else:
            return False
    return True
n=int(input())
count=1
num=2
while count<n:
    if judge(num)==True:
        count=count+1
    num=num+1
print(num-1)