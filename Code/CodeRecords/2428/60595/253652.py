def Test():
    n=int(input())
    nums=eval("["+input().strip().replace(" ",",")+"]")
    odd=[]
    even=[]
    for x in nums:
        if(x%2==0):
            even.append(x)
        else:
            odd.append(x)
    odd.sort(reverse=True)
    even.sort(reverse=False)
    odd.extend(even)
    print(" ".join(str(x) for x in odd),end=" \n")
if __name__ == "__main__":
    total=int(input())
    for i in range(0,total):
        Test()