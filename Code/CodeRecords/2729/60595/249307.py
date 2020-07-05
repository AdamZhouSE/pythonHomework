def Test():
    #任何数和任何数异或得0
    #0和任何数异或得这个数
    #所以相同的都抵消了，就剩这一个了
    nums=eval(input())
    find=0
    for k in nums:
        find=find^k
    print(find)

if __name__ == "__main__":
    Test()