def find_triangle(lst):
    if len(lst) < 3:
        return 0
    lst = sorted(lst)
    count = 0
    for i in range(0,len(lst)-2):
        for j in range(i+1,len(lst)-1):
            for k in range(j+1,len(lst)):
                if lst[i]+lst[j] > lst[k]:
                    count = count + 1
                else:
                    break
    return count

if __name__ == "__main__":
    n = int(input())
    ans = []
    for i in range(0,n):
        no = int(input())
        line = input()
        lst = list(map(int, line.split()))
        res = find_triangle(lst)
        ans.append(res)
    for num in ans:
        print(num)