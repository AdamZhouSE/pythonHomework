def find_index(lst1,lst2,lst3,size):
    count = 0
    for i in range(size):
        if lst1[i] - lst2[i] in lst3:
            count += 1
    return count

if __name__ == "__main__":
    testNO = int(input())
    ans = []
    for i in range(testNO):
        n = int(input())
        lst1 = list(map(int,input().split()))
        lst2 = list(map(int, input().split()))
        lst3 = list(map(int, input().split()))
        ans.append(find_index(lst1,lst2,lst3,n))
    for res in ans:
        print(res)