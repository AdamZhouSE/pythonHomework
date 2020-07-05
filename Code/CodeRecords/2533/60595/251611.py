def Test():
    nums=eval(input())
    odd=[]
    even=[]
    for x in nums:
        if(x%2==0):
            even.append(x)
        else:
            odd.append(x)
    even.extend(odd)
    print(even)
if __name__ == "__main__":
    Test()