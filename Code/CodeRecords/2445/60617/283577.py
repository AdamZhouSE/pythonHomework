def main():
    inp=input().split(", ")
    first=inp[0].split(" = ")[1]
    second=inp[1].split(" = ")[1]
    first=first[1:len(first)-1]
    second=second[1:len(second)-1]
    arr1=[]
    arr2=[]
    for letter in first:
        arr1.append(letter)
    for letter in second:
        arr2.append(letter)
    arr1.sort()
    arr2.sort()
    first="".join(arr1)
    second="".join(arr2)
    print("true" if first==second else "false")

if __name__=='__main__':
    main()
