def main():
    li=list(map(int, eval(input())))
    result=[]
    for i in range(0, len(li)-1):
        count=0
        for j in range(i+1, len(li)):
            if li[j]<li[i]:
                count+=1
        result.append(count)
    result.append(0)
    print(result)

if __name__=='__main__':
    main()
        