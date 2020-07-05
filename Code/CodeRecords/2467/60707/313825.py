if __name__ == "__main__":
    n = int(input())
    for i in range(n):
        inp1 = input().split()
        idx = int(inp1[2])
        list1 = input().split(" ")
        for j in range(len(list1)):
            list1[j] = int(list1[j])
        list2 = input().split(" ")
        for k in range(len(list2)):
            list2[k] = int(list2[k])
        list1.extend(list2)
        list1.sort()
        print(list1[idx-1])