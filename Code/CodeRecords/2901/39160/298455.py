n = int(input())

bin_n=bin(n)
print(bin_n.find("11")==-1 and bin_n.find("00")==-1)

 