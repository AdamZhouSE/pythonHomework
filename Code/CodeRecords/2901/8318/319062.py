n = int(input())
bin_n=bin(n)
if bin_n.find("11")==-1 and bin_n.find("00")==-1:
    print("True")

else:
    print("False")