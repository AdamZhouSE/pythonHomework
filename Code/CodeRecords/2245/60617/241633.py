def main():
    Dec=int(input())
    Bin=bin(Dec)[2:].split("")
    idx=[i for i,x in enumerate(Bin) if x=="1"]
    if len(idx)==1 or len(idx)==0:
        print(0)
    else:
        print(max(idx)-min(idx))
    
    

if __name__ == '__main__':
    main()