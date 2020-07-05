def func(list1,idx):
    for k in list1:
        for j in list1:
            if k + j == idx:
                return "Yes"
    return "N0"


if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        inp1 = input().split()
        idx = int(inp1[1])
        list1 = input().split(" ")
        for j in range(len(list1)):
            list1[j] = int(list1[j])
        print(func(list1,idx))