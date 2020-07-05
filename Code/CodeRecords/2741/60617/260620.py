def main():
    arr=eval(input())
    maxLen=1
    for i in range(0, len(arr)):
        Length=1
        for j in range(i+1, len(arr)):
            if arr[j]>=arr[i]:
                Length+=1
            else:
                break
        if Length>maxLen:
            maxLen=Length
    print(maxLen)
    
if __name__=='__main__':
    main()