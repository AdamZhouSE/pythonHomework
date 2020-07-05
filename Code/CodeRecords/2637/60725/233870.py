class Solution {
public:
    int peakIndexInMountainArray(vector<int>& A) 
    {
        int index =0;
        for(int i=0;i<A.size();i++)
        {
            if(A[i]>A[i+1])
            {
                index = i;
                break;
            }
        }
        return index;
    }
};


















作者：好吃红薯
链接：https://www.jianshu.com/p/e09696f88aa4
来源：简书
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
　　
    