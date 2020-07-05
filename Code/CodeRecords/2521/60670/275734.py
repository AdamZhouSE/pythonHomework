barcodes=eval(input())
n=len(barcodes)
answer=[0 for i in range(0,n)]
num_of_barcode={}
for barcode in barcodes:
    if barcode in num_of_barcode:
        num_of_barcode[barcode]+=1
    else:
        num_of_barcode[barcode]=1
barlist=sorted(num_of_barcode.items(),key=lambda x:-x[1])
tmp=[]
for i in barlist:
    for j in range(0,i[1]):
        tmp.append(i[0])
ptr=0
for i in range(0,n,2):
    answer[i]=tmp[ptr]
    ptr+=1
for i in range(1,n,2):
    answer[i]=tmp[ptr]
    ptr+=1
print(answer)