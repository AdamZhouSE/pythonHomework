def find_k(numlst,tar):
    for no in numlst:
        if no == tar:
            return True
    return False

if __name__ == "__main__":
    numlst = list(map(int,input().split(',')))
    tar = int(input())
    print(find_k(numlst,tar))