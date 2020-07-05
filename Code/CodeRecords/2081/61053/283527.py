def count(a,b):
    count = 0
    for i in range(len(a)-len(b)+1):
        flag = True
        for j in range(len(b)):
            if a[i+j] != b[j]:
                flag = False
                break
        if flag:
            count += 1
    return count

if __name__ == "__main__":
    a = input()
    b = input()
    print(count(a,b),end="")