def main():
    arr=eval(input())
    maxLen=1
    Length=1
    for i in range(1, len(arr)):

        if arr[i]>=arr[i-1]:
            Length+=1
        else:
            Length=1
            continue
        # for j in range(i+1, len(arr)):
        #     if arr[j]>=arr[j-1]:
        #         Length+=1
        #     else:
        #         break
        if Length>maxLen:
            maxLen=Length
    print(maxLen)

if __name__=='__main__':
    main()


