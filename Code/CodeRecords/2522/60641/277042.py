def main():
    arr1 = eval(input())
    arr2 = eval(input())
    result = []
    for i in range(0, len(arr2)):
        while arr2[i] in arr1:
            j = arr1.index(arr2[i])
            result.append(arr1[j])
            del arr1[j]
    arr1 = sorted(arr1)
    result = result + arr1
    print(result)


if __name__ == "__main__":
    main()