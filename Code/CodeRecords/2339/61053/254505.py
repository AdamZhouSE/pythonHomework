def find_inverse(num):
    count = 0
    for i in range(0,len(num)):
        for j in range(i+1,len(num)):
            if num[i] > num[j]:
                count = count + 1
    return count

if __name__ == "__main__":
    testNo = int(input())
    ans = []
    for i in range(0,testNo):
        n = input()
        lst = list(map(int,input().split()))
        ans.append(find_inverse(lst))
    for i in ans:
        print(i)