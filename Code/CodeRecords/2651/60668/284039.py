def linerlist_14_swap(string):
    string = string[2:]
    if len(string)%2 != 0:
        string = "0"+string
    re = ""
    for i in range(0,len(string)-1,2):
        re = re+string[i+1]+string[i]
    print(int(re,2))
if __name__=='__main__':
    for _ in range(int(input())):
        n = input()
        linerlist_14_swap(bin(int(n)))