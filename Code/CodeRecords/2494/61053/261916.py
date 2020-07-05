if __name__ == "__main__":
    lst = eval(input())
    ans = 0
    for i in range(0,len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i] > 2*lst[j]:
                ans = ans + 1
    print(ans)