class Solution :
    def kobe(self):
        barcodes = list(input())
        barcodes.sort()
        i = 0
        while i < barcodes.__len__()-2 :
            if barcodes[i] == barcodes[i+1] :
                barcodes.insert(i+1, barcodes[-1])
                del barcodes[-1]
                i += 2
            else:
                i += 1
        if i == barcodes.__len__()-2 :
            if barcodes[i] == barcodes[i+1] :
                barcodes.insert(i+1, barcodes[0])
                del barcodes[0]
        print(barcodes)
so = Solution()
so.kobe()